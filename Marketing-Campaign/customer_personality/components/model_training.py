import os
import sys
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from customer_personality.logger.log import logging
from sklearn.cluster import KMeans
from sklearn import metrics
from customer_personality.exception.exception_handler import AppException
from customer_personality.config.configuration import AppConfiguration

class ModelTrainer:
    def __init__(self, app_config = AppConfiguration()):
        try:
            self.model_trainer_config = app_config.get_model_trainer_config()
        except Exception as e:
            raise AppException(e, sys) from e

    
    def train(self):
        try:
            #loading data
            final_df = pd.read_csv(self.model_trainer_config.transformed_data_file_dir)
            
            # Lets see how many cluster we should keep using Elbow Method
            clusterRange = range(2,21)
            inertiaRange = []
            silhouterange = []

            for m in clusterRange:
                model_m = KMeans(n_clusters=m)
                model_m.fit(final_df)
                inertiaRange.append(model_m.inertia_)
                silhouterange.append(metrics.silhouette_score(final_df, model_m.labels_))

            os.makedirs(self.model_trainer_config.trained_model_dir, exist_ok=True) 
            plt.plot(clusterRange, inertiaRange)
            image_name = os.path.join(self.model_trainer_config.trained_model_dir,"elbow_plot.png")
            # plt.savefig(image_name)
            
            # cluster 4 is fine for this data
            model = KMeans(n_clusters=4)
            model.fit(final_df)

            #Saving model object for recommendations
            os.makedirs(self.model_trainer_config.trained_model_dir, exist_ok=True)
            file_name = os.path.join(self.model_trainer_config.trained_model_dir,self.model_trainer_config.trained_model_name)
            pickle.dump(model,open(file_name,'wb'))
            logging.info(f"Saving final model to {file_name}")
            
        except Exception as e:
            raise AppException(e, sys) from e

    
    def initiate_model_trainer(self):
        try:
            logging.info(f"{'='*20}Model Trainer log started.{'='*20} ")
            self.train()
            logging.info(f"{'='*20}Model Trainer log completed.{'='*20} \n\n")
        except Exception as e:
            raise AppException(e, sys) from e
