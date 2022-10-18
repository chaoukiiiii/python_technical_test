import pandas as pd


def load_data(file_path: str, filetype="", encoding="utf-8") -> object:
    """
    Load data given its path and filetype, raise error when type not in ["csv","json"]
    """
    if filetype == "csv":
        df = pd.read_csv(file_path, encoding=encoding, sep=",")
        return df
    if filetype == "json":
        df = pd.read_json(file_path, encoding=encoding, orient=str)
        return df
    else:
        raise NotImplementedError


def save_json(df, ouput_file_path):
    """
    save pandas dataframe to json format
    """
    df.to_json(ouput_file_path, orient="records", lines=True)
