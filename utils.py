import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
import sys
import os

def load(path: str):
    ret = None

    try:
        if (isinstance(path, str) is False):
            raise ValueError("Path must be a string")
        if (path.endswith(".csv") is False):
            raise ValueError("Path must be a csv file")
        if (os.path.exists(path) is False):
            raise ValueError("File not found")
        ret = pd.read_csv(path)
    except Exception as e:
        print(e)
    return ret

def remove_columns(df: pd.DataFrame, columns: list):
    ret = df

    try:
        if (isinstance(df, pd.DataFrame) is False):
            raise ValueError("df must be a DataFrame")
        if (isinstance(columns, list) is False):
            raise ValueError("columns must be a list")
        if (len(columns) == 0):
            raise ValueError("columns must have at least one element")
        for col in columns:
            if (col not in df.columns):
                raise ValueError("Column not found")
        ret = df.drop(columns, axis=1)
    except Exception as e:
        print(e)
    return ret

def clean_df_replace_na(df: pd.DataFrame, value: float):
    cleaned_df = remove_columns(df, ["Index", "Hogwarts House"])
    cleaned_df = cleaned_df.select_dtypes(include=['number'])
    cleaned_df = cleaned_df.fillna(value)
    return cleaned_df

def clean_df(df: pd.DataFrame):
    cleaned_df = remove_columns(df, ["Index"])
    cleaned_df = cleaned_df.select_dtypes(include=['number'])
    cleaned_df = cleaned_df.dropna(ignore_index=True)
    return cleaned_df

def clean_df_keep_house(df: pd.DataFrame):
    cleaned_df = remove_columns(df, ["Index"])
    numeric_df = cleaned_df.select_dtypes(include=['number'])

    if 'Hogwarts House' in cleaned_df.columns:
        cleaned_df = pd.concat([numeric_df, cleaned_df[['Hogwarts House']]], axis=1)
    else:
        cleaned_df = numeric_df
    cleaned_df = cleaned_df.dropna(ignore_index=True)
    return cleaned_df

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def standardize(df: pd.DataFrame):
    ret = df
    try:
        if (isinstance(df, pd.DataFrame) is False):
            raise ValueError("Error in standardize: df must be a DataFrame")
        ret = (df - df.mean()) / df.std()
    except Exception as e:
        print(e)
    return ret

def standardize_cols(df):
    for col in df:
        if col != "Hogwarts House":
            df[col] = standardize(df[[col]])
    return df

def get_nb_of_features(df: pd.DataFrame):
    ret = 0
    try:
        if (isinstance(df, pd.DataFrame) is False):
            raise ValueError("Error in get_nb_of_features: df must be a DataFrame")
        for col in df:
            if col != "Hogwarts House":
                ret += 1
    except Exception as e: 
        print(e)
    return ret