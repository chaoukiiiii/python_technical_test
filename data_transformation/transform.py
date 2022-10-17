import pandas as pd

def df_tolist(df,col):
    return [each_string.lower() for each_string in df[col].tolist()]

def df_col_to_lower(df,cols_input,cols_output):
    for cursor in range(0,len(cols_input)):
        df[cols_output[cursor]]=df[cols_input[cursor]].str.lower()
    return df
def drug_in_title(df,col,l):
    df["drug"]=df[col].apply(lambda x: list(set(x.split()) & set(l)))
    return df
def explode_df_col(df,col):
    df=df.explode(col)
    return df

def filter_null_col(df,col):
    df=df[df[col].notnull()]
    return df
def delete_unused_col(df,cols):
    for col in cols:
        del df[col]
    return df
def group_by_cols(df,cols_group,cols_grouped,index_col):
    df_out=df.groupby(cols_group)[cols_grouped].apply(lambda g: g.reset_index(drop=True).T.to_dict('dict')).reset_index(name = index_col)
    return df_out
def merge_df(df_right,df_left,col_right,col_left,how,suffixes):
    return df_left.merge(df_right, left_on=col_left, right_on=col_right, how=how,
          suffixes=suffixes)
    

