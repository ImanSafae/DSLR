from utils import *

def sigmoid_with_params(x, params, bias):
    return 1 / (1 + np.exp(-(np.dot(x, params)) + bias))

def standardize_cols(df):
    for col in df:
        if col != "Hogwarts House":
            df[col] = standardize(df[[col]])
    return df

def log_loss(y, y_pred):
    total = len(y)
    return -np.sum(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred)) / total

def train_for_house(df, house, nb_of_features):
    weights = np.random.rand(nb_of_features)
    bias = 0
    learning_rate = 0.01
    y = df["Hogwarts House"].apply(lambda x: 1 if x == house else 0)
    x = df.drop("Hogwarts House", axis=1).values
    print("X:", x)
    print("Y:", y)

    epochs = 1000
    for epoch in range(epochs):

        predictions_matrix = sigmoid_with_params(x, weights, bias)
        loss = log_loss(y, predictions_matrix)
        if epoch % 100 == 0:
            print(f"Epoch {epoch} loss: {loss}")
            print("Predictions matrix:", predictions_matrix)
        if loss < 0.1:
            break
        weight_gradients = (1 / len(y)) * np.dot(x.T, (predictions_matrix - y))
        bias_gradient = (1 / len(y)) * np.sum(predictions_matrix - y)

        # Mettre à jour les poids
        weights -= learning_rate * weight_gradients
        bias -= learning_rate * bias_gradient

    

if __name__ == "__main__":
    if len (sys.argv) != 2:
        print("Usage: python logreg_train.py <data_file>")
        sys.exit(1)
    
    df = load(sys.argv[1])
    cleaned_df = clean_df_keep_house(df)
    cleaned_df = standardize_cols(cleaned_df)
    # print("Cleaned and standardized data:\n", cleaned_df)

    nb_of_entries = len(df)
    nb_of_features = get_nb_of_features(cleaned_df)
    # train_set = df[0:int(nb_of_entries*0.7)]
    # test_set = df[int(nb_of_entries*0.7):]

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]


    for house in houses:
        train_for_house(cleaned_df, house, nb_of_features)

