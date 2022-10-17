
from data_preparation.data_prep import data_to_be_processed
    

import logging
from utils import DATASOURCES

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info("start load and clean data pipeline ---------------------:-")
    data_preparation_output = data_prep_pipe(DATASOURCES)
    

