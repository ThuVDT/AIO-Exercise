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


def compute_conditional_probability(train_data):
    y_unique = ['No', 'Yes']
    conditional_probability = []
    list_x_name = []
    for i in range(0, train_data.shape[1]-1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)

        x_conditional_probability = {}
        for x in x_unique:
            prob = {}
            for y in y_unique:
                y_count = len(train_data[train_data[:, -1] == y])
                xy_count = len(
                    train_data[(train_data[:, i] == x) & (train_data[:, -1] == y)])
                prob[y] = xy_count/y_count
            x_conditional_probability[x] = prob

        conditional_probability.append(x_conditional_probability)

    return conditional_probability, list_x_name


conditional_probability, list_x_name = compute_conditional_probability(
    train_data)
print("x1 = ", list_x_name[0])
print("x2 = ", list_x_name[1])
print("x3 = ", list_x_name[2])
print("x4 = ", list_x_name[3])
