import numpy as np
import pandas as pd

def load(path: str):
    ret = None

    try:
        if (isinstance(path, str) is False):
            raise ValueError("Path must be a string")
        if (path.endswith(".csv") is False):
            raise ValueError("Path must be a csv file")
        ret = pd.read_csv(path)
        print("Loading dataset:", ret.shape)
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

def count_rows_in_col(df: pd.DataFrame, col:str):
    ret = None

    try:
        if (isinstance(df, pd.DataFrame) is False):
            raise ValueError("df must be a DataFrame")
        if (isinstance(col, str) is False):
            raise ValueError("col must be a string")
        if (col not in df.columns):
            raise ValueError("Column not found")
        ret = df[col].shape[0]
    except Exception as e:
        print(e)
    return ret

def sum_of_col(df: pd.DataFrame, col:str):
    sum = 0

    try:
        if (isinstance(df, pd.DataFrame) is False):
            raise ValueError("df must be a DataFrame")
        if (isinstance(col, str) is False):
            raise ValueError("col must be a string")
        if (col not in df.columns):
            raise ValueError("Column not found")
        
        for (row) in df[col]:
            if (pd.notna(row)):
                sum += row
    except Exception as e:
        print("Error in sum_of_col:", e)
    return sum

def mean_of_col(df: pd.DataFrame, col:str):
    mean = 0

    try:
        if (isinstance(df, pd.DataFrame) is False):
            raise ValueError("df must be a DataFrame")
        if (isinstance(col, str) is False):
            raise ValueError("col must be a string")
        if (col not in df.columns):
            raise ValueError("Column not found")

        total = sum_of_col(df, col)
        nb_of_cols = count_rows_in_col(df, col)
        mean = total / nb_of_cols
    except Exception as e:
        print("Error in mean_of_col:", e)
    return mean

def min_of_col(df: pd.DataFrame, col:str):
    min = 0

    try:
        if (isinstance(df, pd.DataFrame) is False):
            raise ValueError("df must be a DataFrame")
        if (isinstance(col, str) is False):
            raise ValueError("col must be a string")
        if (col not in df.columns):
            raise ValueError("Column not found")
        
        for (row) in df[col]:
            if (pd.notna(row)):
                if (row < min):
                    min = row
    except Exception as e:
        print("Error in min_of_col:", e)
    return min

def max_of_col(df: pd.DataFrame, col:str):
    max = 0

    try:
        if (isinstance(df, pd.DataFrame) is False):
            raise ValueError("df must be a DataFrame")
        if (isinstance(col, str) is False):
            raise ValueError("col must be a string")
        if (col not in df.columns):
            raise ValueError("Column not found")
        
        for (row) in df[col]:
            if (pd.notna(row)):
                if (row > max):
                    max = row
    except Exception as e:
        print("Error in max_of_col:", e)
    return max

def first_quartile_of_col(df: pd.DataFrame, col: str):
    ret = 0
    try:
        if (isinstance(df, pd.DataFrame) is False):
            raise ValueError("df must be a DataFrame")
        if (isinstance(col, str) is False):
            raise ValueError("col must be a string")
        if (col not in df.columns):
            raise ValueError("Column not found")
        
        df[col] = df[col].sort_values().values
        length = count_rows_in_col(df, col)
        if (length % 2 == 0):
            ret = (df[col][length // 4] + df[col][length // 4 + 1]) / 2
        else:
            ret = df[col][length // 4]
    except Exception as e:
        print("Error in first_quartile_of_col:", e)
    return ret

def third_quartile_of_col(df: pd.DataFrame, col: str):
    ret = 0
    try:
        if (isinstance(df, pd.DataFrame) is False):
            raise ValueError("df must be a DataFrame")
        if (isinstance(col, str) is False):
            raise ValueError("col must be a string")
        if (col not in df.columns):
            raise ValueError("Column not found")
        
        df[col] = df[col].sort_values().values
        length = count_rows_in_col(df, col)
        if (length % 2 == 0):
            ret = (df[col][3 * length // 4] + df[col][3 * length // 4 + 1]) / 2
        else:
            ret = df[col][3 * length // 4]
    except Exception as e:
        print("Error in first_quartile_of_col:", e)
    return ret

def median_of_col(df: pd.DataFrame, col: str):
    ret = 0
    try:
        if (isinstance(df, pd.DataFrame) is False):
            raise ValueError("df must be a DataFrame")
        if (isinstance(col, str) is False):
            raise ValueError("col must be a string")
        if (col not in df.columns):
            raise ValueError("Column not found")
        
        df[col] = df[col].sort_values().values
        length = count_rows_in_col(df, col)
        if (length % 2 == 0):
            ret = (df[col][length // 2] + df[col][length // 2 + 1]) / 2
        else:
            ret = df[col][length // 2]
    except Exception as e:
        print("Error in median_of_col:", e)
    return ret

if __name__ == "__main__":
    df = load("./datasets/dataset_test.csv")
    cleaned_df = remove_columns(df, ["Index", "Hogwarts House", "First Name", "Last Name", "Birthday", "Best Hand"])
    print("sum:", sum_of_col(cleaned_df, "Potions"))
    print("total:", count_rows_in_col(cleaned_df, "Potions"))
    print("mean:", mean_of_col(cleaned_df, "Potions"))
    print("min:", min_of_col(cleaned_df, "Potions"))
    print("max:", max_of_col(cleaned_df, "Potions"))