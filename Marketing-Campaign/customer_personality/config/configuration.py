import os
import sys
from customer_personality.logger.log import logging
from customer_personality.utils.utils import read_yaml_file
from customer_personality.exception.exception_handler import AppException
from customer_personality.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelPredictionConfig
from customer_personality.constant import *


class AppConfiguration:
    def __init__(self, config_file_path: str = CONFIG_FILE_PATH):
        try:
            self.configs_info = read_yaml_file(file_path=config_file_path)
        except Exception as e:
            raise AppException(e, sys) from e

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            data_ingestion_config = self.configs_info['data_ingestion_config']
            artifacts_dir = self.configs_info['artifacts_config']['artifacts_dir']
            dataset_dir = data_ingestion_config['dataset_dir']

            ingested_data_dir = os.path.join(artifacts_dir, dataset_dir, data_ingestion_config['ingested_dir'])
            raw_data_dir = os.path.join(artifacts_dir, dataset_dir, data_ingestion_config['raw_data_dir'])

            response = DataIngestionConfig(
                dataset_download_url = data_ingestion_config['dataset_download_url'],
                raw_data_dir = raw_data_dir,
                ingested_dir = ingested_data_dir
            )

            logging.info(f"Data Ingestion Config: {response}")
            return response

        except Exception as e:
            raise AppException(e, sys) from e

# Data Validation

    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            data_validation_config = self.configs_info['data_validation_config']
            data_ingestion_config = self.configs_info['data_ingestion_config']
            dataset_dir = data_ingestion_config['dataset_dir']
            artifacts_dir = self.configs_info['artifacts_config']['artifacts_dir']
            marketing_campaign_csv_file = data_validation_config['marketing_campaign_csv_file']
            
            marketing_campaign_csv_file_dir = os.path.join(artifacts_dir, dataset_dir, data_ingestion_config['ingested_dir'], marketing_campaign_csv_file)
            
            clean_data_path = os.path.join(artifacts_dir, dataset_dir, data_validation_config['clean_data_dir'])
            serialized_objects_dir = os.path.join(artifacts_dir, data_validation_config['serialized_objects_dir'])

            response = DataValidationConfig(
                clean_data_dir = clean_data_path,
                marketing_campaign_csv_file = marketing_campaign_csv_file_dir,
                serialized_objects_dir = serialized_objects_dir
            )

            logging.info(f"Data Validation Config: {response}")
            return response

        except Exception as e:
            raise AppException(e, sys) from e

# Data Transformation

    def get_data_transformation_config(self) -> DataTransformationConfig:
        try:
            data_transformation_config = self.configs_info['data_transformation_config']
            data_validation_config = self.configs_info['data_validation_config']
            data_ingestion_config = self.configs_info['data_ingestion_config']
            dataset_dir = data_ingestion_config['dataset_dir']
            artifacts_dir = self.configs_info['artifacts_config']['artifacts_dir']
          
            clean_data_file_path = os.path.join(artifacts_dir, dataset_dir, data_validation_config['clean_data_dir'],'clean_data.csv')
            transformed_data_dir = os.path.join(artifacts_dir, dataset_dir, data_transformation_config['transformed_data_dir'])

            response = DataTransformationConfig(
                clean_data_file_path = clean_data_file_path,
                transformed_data_dir = transformed_data_dir
            )

            logging.info(f"Data Transformation Config: {response}")
            return response

        except Exception as e:
            raise AppException(e, sys) from e

# Model Training 

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        try:
            model_trainer_config = self.configs_info['model_trainer_config']
            data_transformation_config = self.configs_info['data_transformation_config']
            data_ingestion_config = self.configs_info['data_ingestion_config']
            dataset_dir = data_ingestion_config['dataset_dir']
            artifacts_dir = self.configs_info['artifacts_config']['artifacts_dir']

          
           
            transformed_data_file_dir = os.path.join(artifacts_dir, dataset_dir, data_transformation_config['transformed_data_dir'], 'transformed_data.csv')
            trained_model_dir = os.path.join(artifacts_dir, model_trainer_config['trained_model_dir'])
            trained_model_name = model_trainer_config['trained_model_name']

            response = ModelTrainerConfig(
                transformed_data_file_dir = transformed_data_file_dir,
                trained_model_dir = trained_model_dir,
                trained_model_name = trained_model_name
            )

            logging.info(f"Model Trainer Config: {response}")
            return response

        except Exception as e:
            raise AppException(e, sys) from e

# Training Pipeline

    def get_prediction_config(self) -> ModelPredictionConfig:
        try:
            model_trainer_config = self.configs_info['model_trainer_config']
            trained_model_name = model_trainer_config['trained_model_name']
            artifacts_dir = self.configs_info['artifacts_config']['artifacts_dir']
            trained_model_dir = os.path.join(artifacts_dir, model_trainer_config['trained_model_dir'])
            
            trained_model_path = os.path.join(trained_model_dir,trained_model_name)
          
            response = ModelPredictionConfig(
                trained_model_path = trained_model_path
            )

            logging.info(f"Model Prediction Config: {response}")
            return response

        except Exception as e:
            raise AppException(e, sys) from e