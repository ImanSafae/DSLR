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
                
                # Extraire les données pour chaque maison
                ravenclaw_data = ft_describe(extract_house(new_df, 'Ravenclaw')[[col]].copy()).loc[['Mean', 'Std']]
                gryffindor_data = ft_describe(extract_house(new_df, 'Gryffindor')[[col]].copy()).loc[['Mean', 'Std']]
                hufflepuff_data = ft_describe(extract_house(new_df, 'Hufflepuff')[[col]].copy()).loc[['Mean', 'Std']]
                slytherin_data = ft_describe(extract_house(new_df, 'Slytherin')[[col]].copy()).loc[['Mean', 'Std']]
                
                # Convertir les données en scalaires
                bars_mean = [
                    float(ravenclaw_data.loc['Mean'].values[0]), 
                    float(gryffindor_data.loc['Mean'].values[0]), 
                    float(hufflepuff_data.loc['Mean'].values[0]), 
                    float(slytherin_data.loc['Mean'].values[0])
                ]
                bars_std = [
                    float(ravenclaw_data.loc['Std'].values[0]), 
                    float(gryffindor_data.loc['Std'].values[0]), 
                    float(hufflepuff_data.loc['Std'].values[0]), 
                    float(slytherin_data.loc['Std'].values[0])
                ]

                # Créer le graphique
                fig, ax = plt.subplots()
                index = np.arange(4)  # Pour 4 maisons
                bar_width = 0.35

                # Dessiner les barres
                ax.bar(index, bars_mean, bar_width, label='Mean', color='blue')
                ax.bar(index + bar_width, bars_std, bar_width, label='Std', color='orange')

                # Personnalisation du graphique
                ax.set_xlabel('Hogwarts House')
                ax.set_ylabel('Scores')
                ax.set_title(f'{col} Statistics by House')
                ax.set_xticks(index + bar_width / 2)
                ax.set_xticklabels(['Ravenclaw', 'Gryffindor', 'Hufflepuff', 'Slytherin'])
                ax.legend()

                # Afficher le graphique
                plt.show()



                
    except Exception as e:
        print(e)