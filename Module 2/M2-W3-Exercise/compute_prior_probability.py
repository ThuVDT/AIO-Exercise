import numpy as np


def create_train_data():
    data = [['Sunny', 'Hot', 'High', 'Weak', 'No'],
            ['Sunny', 'Hot', 'High', 'Strong', 'No'],
            ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
            ['Rain', 'Mid', 'High', 'Weak', 'Yes'],
            ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
            ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
            ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
            ['Overcast', 'Mild', 'High', 'Weak', 'No'],
            ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
            ['Rain', 'Mild', 'Normal', 'Weak', 'Yes']]
    return np.array(data)


train_data = create_train_data()
print(train_data)


def compute_prior_probability(train_data):
    y_unique = ['No', 'Yes']
    prior_probability = np.zeros(len(y_unique))

    for i in range(len(y_unique)):
        prior_probability[i] = len(
            train_data[train_data[:, -1] == y_unique[i]]) / len(train_data)
    return prior_probability


prior_probability = compute_prior_probability(train_data)
print("P(play tenis = No)", prior_probability[0])
print("P(play tenis = Yes)", prior_probability[1])
