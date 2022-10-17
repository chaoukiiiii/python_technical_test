import pandas as pd

import json

############# config
DATASOURCES = ["drugs", "clinical_trials", "pubmed"]
############


def load_datasrc_config(path="datasources_config/config_src.json"):
    """
    Load datasrc configuration given datasrc_name
    """
    config = load_json(path)
    return config


def load_json(filepath):
    """
    load json file
    """
    with open(filepath) as f:
        res_json = json.load(f)
    return res_json


def df_tolist(df, col):
    return [each_string.lower() for each_string in df[col].toList]
