from utils import *

def sigmoid_with_params(x, params):
    return 1 / (1 + np.exp(-(np.dot(x, params))))
    
def standardize_cols(df):
    for col in df:
        if col != "Hogwarts House":
            df[col] = standardize(df[[col]])
    return df

def log_loss(y, y_pred):
    total = len(y)
    return -np.sum(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred)) / total


def get_gradient_descent(y, y_pred, x, index):
    diff = y_pred - y
    dot_product = np.dot(x[:, index], diff)
    gradient = dot_product / y.size
    return gradient

def train_for_house(df, house, nb_of_features):
    try:
        weights = np.random.rand(nb_of_features)
        learning_rate = 0.04
        y = df["Hogwarts House"].apply(lambda x: 1 if x == house else 0)
        x = df.drop("Hogwarts House", axis=1).values

        epochs = 8000
        for epoch in range(epochs):
            predictions_matrix = sigmoid_with_params(x, weights)

            loss = log_loss(y, predictions_matrix)
            if epoch % 500 == 0:
                print(f"Epoch {epoch} loss: {loss}")

            if loss < 0.1:
                print("Epoch: ", epoch)
                print("Loss is less than 0.1: ", loss)
                break

            weight_gradients = []
            for i in range(nb_of_features):
                new_gradient = get_gradient_descent(y, predictions_matrix, x, i)
                weight_gradients.append(new_gradient)

            weight_gradients = np.array(weight_gradients)
            weights -= learning_rate * weight_gradients
        
    except Exception as e:
        print("Error in train_for_house:", e)
    return weights

    

if __name__ == "__main__":
    if len (sys.argv) != 2:
        print("Usage: python logreg_train.py <data_file>")
        sys.exit(1)
    
    df = load(sys.argv[1])
    cleaned_df = clean_df_keep_house(df)
    cleaned_df = standardize_cols(cleaned_df)

    nb_of_entries = len(df)
    nb_of_features = get_nb_of_features(cleaned_df)

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    ret = pd.DataFrame(columns=cleaned_df.columns, index=houses)
    ret.drop("Hogwarts House", axis=1, inplace=True)
    for house in houses:
        weights = train_for_house(cleaned_df, house, nb_of_features)
        ret.loc[house] = weights
    print(ret)

