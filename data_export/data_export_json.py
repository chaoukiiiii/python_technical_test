


import pandas as pd



def export_tojson_pipe(df,path):
    df.to_json(path+'/resulut.json', orient='records', lines=True)