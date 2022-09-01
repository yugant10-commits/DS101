from typing import List
import pandas as pd

def start_pipeline(
    df: pd.DataFrame
    )->pd.DataFrame:
    return df.copy()

def clean_col_spaces(
    df:pd.DataFrame
    )->pd.DataFrame:
    df.columns = [names.replace(" ", "") for names in df]
    return df

def delete_cols(
    df:pd.DataFrame, 
    columns_to_delete:List
    )->pd.DataFrame:
  return df.drop(columns_to_delete,axis=1)

def convert_to_date(
    df: pd.DataFrame, 
    date_columns: List 
    )->pd.DataFrame:
    df[date_columns] = df[date_columns].astype("datetime64")
    return df