import pandas as pd


def export_tojson_pipe(df, path):
    """
    this function export dataframe to json file
    
    """
    df.to_json(path + "/result.json", orient="records", lines=True)
