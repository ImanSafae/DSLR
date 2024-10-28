from utils import *

def pairplot(df):
    sns.pairplot(df)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pair_plot.py <data_file>")
        sys.exit(1)

    df = load(sys.argv[1])
    cleaned_df = clean_df(df)
    pairplot(cleaned_df)