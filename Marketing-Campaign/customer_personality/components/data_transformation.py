import os
import sys
import pandas as pd
from customer_personality.logger.log import logging
from customer_personality.exception.exception_handler import AppException
from customer_personality.config.configuration import AppConfiguration



class DataTransformation:
    def __init__(self, app_config = AppConfiguration()):
        try:
            self.data_transformation_config = app_config.get_data_transformation_config()
        except Exception as e:
            raise AppException(e, sys) from e

    

    def get_data_transformer(self):
        try:
            df = pd.read_csv(self.data_transformation_config.clean_data_file_path)
            final_df = df.drop(
                [
                'ID', 'Year_Birth','Education','Marital_Status', 'Kidhome', 
                'Teenhome', 'Dt_Customer', 'MntWines', 'MntFruits', 'MntMeatProducts',
                    'MntFishProducts', 'MntSweetProducts','MntGoldProds','NumDealsPurchases',
                    'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases','NumWebVisitsMonth',
                    'AcceptedCmp3','AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1',
                    'AcceptedCmp2', 'Complain', 'Z_CostContact', 'Z_Revenue', 'Response','AgeGroup'
                ],
                
                axis = 1
            )

            #saving personality data
            os.makedirs(self.data_transformation_config.transformed_data_dir, exist_ok=True)
            final_df.to_csv(os.path.join(os.path.join(self.data_transformation_config.transformed_data_dir),"transformed_data.csv"), index = False)
            logging.info(f"Saved personality data to {self.data_transformation_config.transformed_data_dir}")

            
        except Exception as e:
            raise AppException(e, sys) from e


    def initiate_data_transformation(self):
        try:
            logging.info(f"{'='*20}Data Transformation log started.{'='*20} ")
            self.get_data_transformer()
            logging.info(f"{'='*20}Data Transformation log completed.{'='*20} \n\n")
        except Exception as e:
            raise AppException(e, sys) from e
