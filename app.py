import sys
import os

# Add the "src" folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "src")))

from mlproject.logger import logging



from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys



if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)



