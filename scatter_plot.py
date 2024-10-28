from utils import *

def create_scatter_plot_pairs(df: pd.DataFrame):
    subjects = ['Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying']
    i = 0
    j = 0
    try:
        while i < len(subjects):
            while j < len(subjects):
                if i != j:
                    plt.scatter(df[subjects[i]], df[subjects[j]])
                    plt.xlabel(subjects[i])
                    plt.ylabel(subjects[j])
                    plt.title(f"{subjects[i]} vs {subjects[j]}")
                    plt.show()
                j += 1
            i += 1
            j = i
    except Exception as e:
        print(e)
        sys.exit(1)
        



if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: python3 scatter_plot.py <csv file>")
        sys.exit(1)

    df = load(sys.argv[1])
    cleaned_df = clean_df(df)
    create_scatter_plot_pairs(cleaned_df)


