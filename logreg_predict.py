from utils import *
from sklearn.metrics import accuracy_score

def get_house_probability(house, data, house_weights):
    z = np.dot(data, house_weights)
    proba = sigmoid(z)
    return proba


def predict(data, houses, weights):
    predictions = pd.DataFrame(columns=["Hogwarts House"])
    for index, row in data.iterrows():
        probabilities = {}
        for i in range(len(houses)):
            house_proba = get_house_probability(houses[i], row, weights.loc[houses[i]])
            probabilities[houses[i]] = house_proba
        max_house = ""
        max_proba = 0
        for key, value in probabilities.items():
            if value > max_proba:
                max_house = key
                max_proba = value
        predictions.loc[len(predictions)] = max_house
    return predictions
        


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python logreg_predict.py <data_file>")
        sys.exit(1)
    data = load(sys.argv[1])
    weights = pd.read_csv("weights.csv", index_col=0)
    if (data is None):
        print("Given data in wrong format.")
        sys.exit(1)

    houses = ["Gryffindor", "Ravenclaw", "Slytherin", "Hufflepuff"]
    if data is None:
        sys.exit(1)
    data = clean_df_replace_na(data, 0)
    data = standardize_cols(data)
    predictions = predict(data, houses, weights)
    with open("houses.csv", "w") as outfile:
        predictions.to_csv(outfile)
    
    test_data = pd.read_csv('datasets/dataset_train.csv')
    predicted_data = pd.read_csv('houses.csv')
    true_labels = test_data['Hogwarts House']
    predicted_labels = predicted_data['Hogwarts House']
    accuracy = accuracy_score(true_labels, predicted_labels)
    print(f"L'accuracy de votre modèle est : {accuracy * 100:.2f}%")
