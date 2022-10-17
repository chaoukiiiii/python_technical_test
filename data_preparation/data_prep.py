from data_preparation.clean import clean_df
from data_preparation.load import load_data
from utils import load_datasrc_config
import pandas as pd


def data_prep_pipe(data_src: list[str]):
    dict_df = dict()
    for src in data_src:
        output_df = data_to_be_processed(src)
        dict_df[src] = output_df
    return dict_df


def data_to_be_processed(src: str):
    config = load_datasrc_config()
    if len(config[src]["file_source"]["type"]) == 1:
        path = (
            config[src]["file_source"]["path"]
            + config[src]["file_source"]["file_name"][0]
        )
        type_file = config[src]["file_source"]["type"][0]
        df_src = load_data(path, filetype=type_file)
        df_clean = clean_df(df_src, config[src]["file_prepocess"])
        return df_clean
    elif len(config[src]["file_source"]["type"]) == 2:
        df_src = pd.DataFrame()
        cursor = 0
        for type_file in config[src]["file_source"]["type"]:
            path = (
                config[src]["file_source"]["path"]
                + config[src]["file_source"]["file_name"][cursor]
            )
            df_tmp = load_data(path, filetype=type_file)
            df_src = pd.concat([df_src, df_tmp])
            cursor = cursor + 1
        df_clean = clean_df(df_src, config[src]["file_prepocess"])
        return df_clean
    else:
        raise NotImplementedError
