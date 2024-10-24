from utils import *
from describe import ft_describe

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

        for col in cleaned_df.columns: 
            if col != 'Hogwarts House':
                print("Column:", col)

                # Extraire la colonne + Hogwarts House dans un nouveau dataframe
                new_df = cleaned_df[[col, 'Hogwarts House']]
                
                ravenclaw_values = (extract_house(new_df, 'Ravenclaw')).values.tolist()
                gryffindor_values = (extract_house(new_df, 'Gryffindor')).values.tolist()
                hufflepuff_values = (extract_house(new_df, 'Hufflepuff')).values.tolist()
                slytherin_values = (extract_house(new_df, 'Slytherin')).values.tolist()

                print("ravenclaw values:\n", ravenclaw_values)
                print("gryffindor values:\n", gryffindor_values)
                print("hufflepuff values:\n", hufflepuff_values)
                print("slytherin values:\n", slytherin_values)



                
    except Exception as e:
        print(e)