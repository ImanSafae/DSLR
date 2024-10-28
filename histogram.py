from utils import *

def extract_house(df: pd.DataFrame, house: str):
    houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    ret = None
    try:
        if (df.shape[1] != 2):
            raise ValueError("Dataframe must have 2 columns: one for the feature and one for the house")
        if (house not in houses):
            raise ValueError("House not found")
        if (df.columns[1] != 'Hogwarts House'):
            raise ValueError("Second column must be 'Hogwarts House'")
        
        ret = df[df['Hogwarts House'] == house].reset_index(drop=True)
        ret = ret.drop(columns=['Hogwarts House'])
    except Exception as e:
        print(e)
    return ret

def draw_hists(cleaned_df: pd.DataFrame):
    subjects = ['Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying']
    houses = ['Ravenclaw', 'Gryffindor', 'Hufflepuff', 'Slytherin']
    try:
        for col in cleaned_df:
            if col not in subjects:
                continue
            new_df = cleaned_df[[col, 'Hogwarts House']]
                
            ravenclaw_values = (extract_house(new_df, 'Ravenclaw'))
            gryffindor_values = (extract_house(new_df, 'Gryffindor'))
            hufflepuff_values = (extract_house(new_df, 'Hufflepuff'))
            slytherin_values = (extract_house(new_df, 'Slytherin'))

            _= plt.hist(ravenclaw_values[col], bins=10, color=(21/255, 0, 1, 0.5), label='Ravenclaw')
            _ = plt.hist(gryffindor_values[col], bins=10, color=(237/255, 40/255, 40/255, 0.5), label='Gryffindor')
            _ = plt.hist(hufflepuff_values[col], bins=10, color=(242/255, 231/255, 21/255, 0.5), label='Hufflepuff')
            _ = plt.hist(slytherin_values[col], bins=10, color=(43/255, 124/255, 32/255, 0.5), label='Slytherin')
            _ = plt.xlabel("Grades")
            _ = plt.ylabel("Frequency")
            _ = plt.title(col)
            _ = plt.legend()
            plt.show()
    except Exception as e:
        print(e)
        sys.exit(1)
        

if __name__ == "__main__":
    labels = ['Ravenclaw', 'Gryffindor', 'Hufflepuff', 'Slytherin']
    try:
        if (len(sys.argv) != 2):
            raise ValueError("Usage: python3 histogram.py <csv file>")
        if (os.path.exists(sys.argv[1]) is False):
            raise ValueError("File not found")
        if (sys.argv[1].endswith(".csv") is False):
            raise ValueError("File must be a csv file")
        
        df = load(sys.argv[1])

        if (df is None):
            print("Failed to load data")
            sys.exit(1)

        cleaned_df = clean_df(df)
        if 'Hogwarts House' in cleaned_df.columns or 'Hogwarts House' in df.columns:
            cleaned_df['Hogwarts House'] = df['Hogwarts House']

        print("cleaned_df:\n", cleaned_df.shape)

        # for col in cleaned_df.columns: 
        #     if col != 'Hogwarts House':
        #         print("Column:", col)

        #         # Extraire la colonne + Hogwarts House dans un nouveau dataframe
        #         new_df = cleaned_df[[col, 'Hogwarts House']]
                
        #         ravenclaw_values = (extract_house(new_df, 'Ravenclaw'))
        #         gryffindor_values = (extract_house(new_df, 'Gryffindor'))
        #         hufflepuff_values = (extract_house(new_df, 'Hufflepuff'))
        #         slytherin_values = (extract_house(new_df, 'Slytherin'))

        #         _= plt.hist(ravenclaw_values[col], bins=10, color=(21/255, 0, 1, 0.5), label='Ravenclaw')
        #         _ = plt.hist(gryffindor_values[col], bins=10, color=(237/255, 40/255, 40/255, 0.5), label='Gryffindor')
        #         _ = plt.hist(hufflepuff_values[col], bins=10, color=(242/255, 231/255, 21/255, 0.5), label='Hufflepuff')
        #         _ = plt.hist(slytherin_values[col], bins=10, color=(43/255, 124/255, 32/255, 0.5), label='Slytherin')
        #         _ = plt.xlabel("Grades")
        #         _ = plt.ylabel("Frequency")
        #         _ = plt.title(col)
        #         _ = plt.legend()
        #         plt.show()
        draw_hists(cleaned_df)



                
    except Exception as e:
        print(e)