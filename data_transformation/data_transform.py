from data_transformation.transform import *
import pandas as pd


def data_transform_pipe(df_dict):
    df_drug = df_dict["drugs"]
    list_of_drug = df_tolist(df_drug, "drug")
    if "pubmed" in df_dict.keys():
        df_dict["pubmed"] = extract_drug(
            df_dict["pubmed"], list_of_drug, "title", "pubmed"
        )
    if "clinical_trials" in df_dict.keys():
        df_dict["clinical_trials"] = extract_drug(
            df_dict["clinical_trials"], list_of_drug, "title", "clinical_trials"
        )
    df_final = merge_df(
        df_dict["pubmed"],
        df_dict["clinical_trials"],
        ["drug", "journal"],
        ["drug", "journal"],
        "outer",
        ("pubmed", "clinical_trials"),
    )
    return df_final


def extract_drug(df, l, col_title, col_index):
    col_title_output = col_title + "_lower"
    df = df_col_to_lower(df, [col_title], [col_title_output])
    df = drug_in_title(df, col_title_output, l)
    df = explode_df_col(df, "drug")
    df = filter_null_col(df, "drug")
    df = delete_unused_col(df, [col_title_output])
    df = group_by_cols(df, ["drug", "journal"], ["id", "date", "title"], col_index)
    return df
