import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO)

project_name="mlproject"


list_of_files=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/feature_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/components/training_pipeline.py",
    f"src/{project_name}/components/prediction_pipeline.py",
    f"src/{project_name}/components/exception.py",
    f"src/{project_name}/components/logger.py",
    f"src/{project_name}/components/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",


]




for file_path in list_of_files:
    filepath=Path(file_path)
    filedir,filename=os.path.split(filepath)


    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory:{filedir} for the file{filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")
