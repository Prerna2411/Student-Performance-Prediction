import os
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.model_trainer import ModelTrainer

def train():
    try:
        logging.info("Starting Training Pipeline")

        # Step 1: Data Ingestion (Load Raw Data)
        data_ingestion = DataIngestion()
        train_path, test_path = data_ingestion.initiate_config()

        # Step 2: Data Transformation (Preprocess Data)
        data_transformation = DataTransformation()
        train_array, test_array = data_transformation.initiate_data_transformation(train_path, test_path)

        # Step 3: Model Training
        model_trainer = ModelTrainer()
        r2_score = model_trainer.initiate_model_trainer(train_array, test_array)

        print(f"Training Completed. Model R² Score: {r2_score}")
        logging.info(f"Training Completed. Model R² Score: {r2_score}")

    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    train()
