import pandas as pd
import pandas as pd
import codecs
import re
import unidecode
import os



def clean_df(df, data_src_config: dict):
    """
    clean dataframe based of json config source file
    """
    if "no_nansvalue" in data_src_config.keys():
        df = filter_nans(df, data_src_config["no_nansvalue"])
    if "remove_special_char" in data_src_config.keys():
        df = remove_special_char(df, data_src_config["remove_special_char"]["columns"])
    if "columns_type" in data_src_config.keys():
        for column_name, column_type in data_src_config["columns_type"].items():
            df = cast_column(df, column_name, column_type)
    if "rename_columns" in data_src_config.keys():
        for column_init_name, column_new_name in data_src_config["rename_columns"].items():
            df = rename_column(df, column_init_name, column_new_name)
    return df


def rename_column(df, column_i_name, column_n_name):
    """
    Rename column in dataframe
    """
    df = df.rename(columns={column_i_name: column_n_name})
    return df


def cast_column(df, column_name, column_type):
    """
    Cast column in dataframe
    """
    if column_type == "date":
        df[column_name] = pd.to_datetime(df[column_name])
    else:
        df[column_name] = df[column_name].astype(column_type)
    return df


def filter_nans(df, cols):
    """
    filter rows that contain nan
    """
    df = df.dropna(subset=cols)
    return df


def remove_special_char(df, list_columns):
    """
    Remove and treat special character from a subset of columns
    """
    for colname in list_columns:
        df[colname].apply(lambda x: remove_str_special_char(x))
    return df


def remove_str_special_char(in_str: str) -> str:
    """
    replace special char in input string with empty str
    """
    f_str = in_str
    try:
        in_str = unidecode.unidecode(in_str)
        in_str = codecs.decode(in_str, "unicode_escape")
        f_str = re.sub(r"[^A-Za-z0-9 ]+", "", in_str)
    except Exception as e:
        print(e)
    return f_str