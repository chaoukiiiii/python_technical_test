
from data_preparation.data_prep import data_to_be_processed
    

import logging
from utils import DATASOURCES

if __name__ == "__main__":

    logging.info("start load data pipeline ---------------------:-")
    data_preparation_output = data_to_be_processed(DATASOURCES)

    print(data_preparation_output)
    

