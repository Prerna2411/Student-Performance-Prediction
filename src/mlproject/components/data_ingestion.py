import os
import sys
import pandas as pd
from src.mlproject.logger import logging
from  src.mlproject.exception import CustomException

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts',"train.csv")
    test_data_path:str=os.path.join('artifacts',"test.csv")
    raw_data_path:str=os.path.join('artifacts','stud.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_config(self):
        logging.info("Entered the data ingestion method")
        try:
            # Read the raw dataset
            df=pd.read_csv('notebook\stud.csv')
            logging.info('Read dataset as dataframe')
            #Create directory if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            ##train test split initiated
            logging.info('Initiating train test split')
            train_set,test_set=train_test_split(df,test_Size=0.2,random_state=42)

            ##save train and test datasets
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info('Train and Test datasets saved')
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)



if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_config()
    data_transformation=DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)
