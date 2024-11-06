from utils import *

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python logreg_predict.py <data_file>")
        sys.exit(1)
    data = load(sys.argv[1])
    weights = load("houses.csv")

    print("weights:\n", weights)
    if data is None:
        sys.exit(1)
    data = clean_df_replace_na(data, 0)
    print("data:\n", data)
