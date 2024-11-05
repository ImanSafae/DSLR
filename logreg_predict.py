from utils import *

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python logreg_predict.py <data_file>")
        sys.exit(1)
    data = load(sys.argv[1])

    if data is None:
        sys.exit(1)
    data = clean_df(data)
    print("data:", data)