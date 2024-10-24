import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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

def clean_df(df: pd.DataFrame):
    cleaned_df = remove_columns(df, ["Index"])
    cleaned_df = cleaned_df.select_dtypes(include=['number'])
    cleaned_df = cleaned_df.dropna(ignore_index=True)
    return cleaned_df