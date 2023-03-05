import os
import sys
import ast 
import pandas as pd
from customer_personality.logger.log import logging
from customer_personality.exception.exception_handler import AppException
from customer_personality.config.configuration import AppConfiguration


class DataValidation:
    def __init__(self, app_config = AppConfiguration()):
        try:
            self.data_validation_config= app_config.get_data_validation_config()
        except Exception as e:
            raise AppException(e, sys) from e

    

    def preprocess_data(self):
        try:
            # loading all the data
            df = pd.read_csv(self.data_validation_config.marketing_campaign_csv_file,  sep='\t')
            logging.info(f" Shape of the data file: {df.shape}")
            #Droping null
            df.dropna(inplace=True)

            # Creating age columns
            df['Age'] = 2015 - df['Year_Birth']
            # Creating age group 
            df.loc[df['Age'] <=19, "AgeGroup"] = "Teen"
            df.loc[(df['Age'] >=20) & (df['Age'] <= 39), "AgeGroup"] = "Adults"
            df.loc[(df['Age'] >=40) & (df['Age'] <= 59), "AgeGroup"] = "Middle Age Adults"
            df.loc[(df['Age'] >= 60), "AgeGroup"] = "Seniors"

            #Creating some extra columns by aggregating them
            df['TotalSpendings'] = df['MntFruits'] + df['MntWines'] + df['MntMeatProducts'] + df['MntFishProducts'] + df['MntSweetProducts'] + df['MntGoldProds']
            df['Children'] = df['Kidhome'] + df['Teenhome']

            df.Marital_Status = df.Marital_Status.replace({
                "Together" : "Married",
                "Divorced" : "Single",
                "Widow" : "Single",
                "Alone" : "Single",
                "Absurd" : "Single",
                "YOLO" : "Single"
            })

            #Converting to datetime
            df.Dt_Customer = pd.to_datetime(df.Dt_Customer)

            
            # MonthEnrollement
            df['MonthEnrollement'] = (2015 - df.Dt_Customer.dt.year) * 12 + (1 - df.Dt_Customer.dt.month)

            #Droping outliers from Age & Income
            df = df[df['Age'] < 100]
            df = df[df['Income'] < 110000]
            logging.info(f" Shape of cleaned data file: {df.shape}")

            # Saving the cleaned data for transformation
            os.makedirs(self.data_validation_config.clean_data_dir, exist_ok=True)
            df.to_csv(os.path.join(self.data_validation_config.clean_data_dir,'clean_data.csv'), index = False)
            logging.info(f"Saved cleaned data to {self.data_validation_config.clean_data_dir}")

        except Exception as e:
            raise AppException(e, sys) from e

    
    
    def initiate_data_validation(self):
        try:
            logging.info(f"{'='*20}Data Validation log started.{'='*20} ")
            self.preprocess_data()
            logging.info(f"{'='*20}Data Validation log completed.{'='*20} \n\n")
        except Exception as e:
            raise AppException(e, sys) from e

    
