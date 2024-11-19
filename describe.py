

from utils import *

def calculate_percentile(data, percentile):
    sorted_data = sorted(map(float, data))

    rank = (percentile / 100.0) * (len(sorted_data) - 1)
    lower_index = int(rank)
    upper_index = lower_index + 1 

    if upper_index >= len(sorted_data):
        return sorted_data[lower_index]
    weight = rank - lower_index
    return sorted_data[lower_index] * (1 - weight) + sorted_data[upper_index] * weight

def iqr_of_col(first_quartile, third_quartile):
    iqr = third_quartile - first_quartile
    return iqr
    

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

def mean_of_col(df: pd.DataFrame, col:str, nb_of_cols: int):
    mean = 0

    try:
        if (isinstance(df, pd.DataFrame) is False):
            raise ValueError("df must be a DataFrame")
        if (isinstance(col, str) is False):
            raise ValueError("col must be a string")
        if (col not in df.columns):
            raise ValueError("Column not found")

        total = sum_of_col(df, col)
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

def first_quartile_of_col(df: pd.DataFrame, col: str, length: int):
    ret = 0
    try:
        if (isinstance(df, pd.DataFrame) is False):
            raise ValueError("df must be a DataFrame")
        if (isinstance(col, str) is False):
            raise ValueError("col must be a string")
        if (col not in df.columns):
            raise ValueError("Column not found")
        df[col] = df[col].sort_values().values
        if (length % 2 == 0):
            ret = (df[col][length // 4] + df[col][length // 4 + 1]) / 2
        else:
            ret = df[col][length // 4]
    except Exception as e:
        print("Error in first_quartile_of_col:", type(e).__name__)
    return ret

def third_quartile_of_col(df: pd.DataFrame, col: str, length: int):
    ret = 0
    try:
        if (isinstance(df, pd.DataFrame) is False):
            raise ValueError("df must be a DataFrame")
        if (isinstance(col, str) is False):
            raise ValueError("col must be a string")
        if (col not in df.columns):
            raise ValueError("Column not found")
        
        df[col] = df[col].sort_values().values
        # length = count_rows_in_col(df, col)
        if (length % 2 == 0):
            ret = (df[col][3 * length // 4] + df[col][3 * length // 4 + 1]) / 2
        else:
            ret = df[col][3 * length // 4]
    except Exception as e:
        print("Error in first_quartile_of_col:", type(e).__name__)
    return ret

def median_of_col(df: pd.DataFrame, col: str, length: int):
    ret = 0
    try:
        if (isinstance(df, pd.DataFrame) is False):
            raise ValueError("df must be a DataFrame")
        if (isinstance(col, str) is False):
            raise ValueError("col must be a string")
        if (col not in df.columns):
            raise ValueError("Column not found")
        
        df[col] = df[col].sort_values().values
        if (length % 2 == 0):
            ret = (df[col][length // 2] + df[col][length // 2 + 1]) / 2
        else:
            ret = df[col][length // 2]
    except Exception as e:
        print("Error in median_of_col:", type(e).__name__)
    return ret

def standard_deviation_of_col(df: pd.DataFrame, col: str, length: int):
    ret = 0
    try:
        if (isinstance(df, pd.DataFrame) is False):
            raise ValueError("df must be a DataFrame")
        if (isinstance(col, str) is False):
            raise ValueError("col must be a string")
        if (col not in df.columns):
            raise ValueError("Column not found")
        mean = mean_of_col(df, col, length)
        sum_of_squares = 0

        for row in df[col]:
            if (pd.notna(row)):
                sum_of_squares += (row - mean) ** 2
        var = sum_of_squares / length
        ret = math.sqrt(var) 
    except Exception as e:
        print("Error in standard_deviation_of_col:", e)
    return ret

def ft_describe(df: pd.DataFrame):
    ret = None
    try:
        if (isinstance(df, pd.DataFrame) is False):
            raise ValueError("df must be a DataFrame")
        
        for col in df.columns:
            length = count_rows_in_col(df, col)
            mean = mean_of_col(df, col, length)
            std = standard_deviation_of_col(df, col, length)
            min = min_of_col(df, col)
            first_quartile = first_quartile_of_col(df, col, length)
            median = median_of_col(df, col, length)
            third_quartile = third_quartile_of_col(df, col, length)
            max = max_of_col(df, col)
            iqr  = iqr_of_col(first_quartile, third_quartile)
            rows = [length, mean, std, min, first_quartile, median, third_quartile, max, iqr]
            if (ret is None):
                ret = pd.DataFrame({col: rows})
                ret.index = ["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max","IQR"]
            else:
                ret.insert(len(ret.columns), col, rows)
    except Exception as e:
        print("Error in ft_describe:", e)
    return ret

# def clean_df(df: pd.DataFrame):
#     cleaned_df = remove_columns(df, ["Index"])
#     cleaned_df = cleaned_df.select_dtypes(include=['number'])
#     cleaned_df = cleaned_df.dropna(ignore_index=True)
#     return cleaned_df

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python describe.py <path>")
        sys.exit(1)
    df = load(sys.argv[1])
    if (df is None):
        sys.exit(1)

    cleaned_df = clean_df(df)
    print(ft_describe(cleaned_df))
    # print('---------------------------')
    # print(cleaned_df.describe())

