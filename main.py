from data_preparation.data_prep import data_prep_pipe
from data_transformation.data_transform import data_transform_pipe
from data_export.data_export_json import export_tojson_pipe
import logging

logging.info("Admin logged in")
from utils import DATASOURCES

if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
    logging.info("start load and clean data pipeline ---------------------:-")
    data_preparation_output = data_prep_pipe(DATASOURCES)

    logging.info("start transform pipeline ---------------------:-")
    data_transformation_output = data_transform_pipe(data_preparation_output)
    logging.info("start export json pipeline ---------------------:-")
    export_tojson_pipe(data_transformation_output, "output")
