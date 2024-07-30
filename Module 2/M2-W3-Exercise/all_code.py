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


def compute_prior_probability(train_data):
    y_unique = ['No', 'Yes']
    prior_probability = np.zeros(len(y_unique))

    for i in range(len(y_unique)):
        prior_probability[i] = len(
            train_data[train_data[:, -1] == y_unique[i]]) / len(train_data)
    return prior_probability


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


def get_index_from_value(feature_name, list_features):
    indices = np.nonzero(list_features == feature_name)[0]
    if indices.size > 0:
        return indices[0]
    else:
        raise ValueError(f"{feature_name} not found in list_features")


train_data = create_train_data()
_, list_x_name = compute_conditional_probability(train_data)
outlook = list_x_name[0]

i1 = get_index_from_value("Overcast", outlook)
i2 = get_index_from_value("Rain", outlook)
i3 = get_index_from_value("Sunny", outlook)
print(i1, i2, i3)


def train_naive_bayes(train_data):
    prior_probability = compute_prior_probability(train_data)
    conditional_probability, list_x_name = compute_conditional_probability(
        train_data)
    return prior_probability, conditional_probability, list_x_name


def prediction_play_tennis(x, prior_probability, conditional_probability):

    p0 = prior_probability[0]
    p1 = prior_probability[1]

    p0 *= conditional_probability[0][x[0]]['No']
    p0 *= conditional_probability[1][x[1]]['No']
    p0 *= conditional_probability[2][x[2]]['No']
    p0 *= conditional_probability[3][x[3]]['No']

    p1 *= conditional_probability[0][x[0]]['Yes']
    p1 *= conditional_probability[1][x[1]]['Yes']
    p1 *= conditional_probability[2][x[2]]['Yes']
    p1 *= conditional_probability[3][x[3]]['Yes']

    if p0 > p1:
        y_pred = 0
    else:
        y_pred = 1

    return y_pred


X = ['Sunny', 'Cool', 'High', 'Strong']
data = create_train_data()
prior_probability, conditional_probability, list_x_name = train_naive_bayes(
    data)
pred = prediction_play_tennis(
    X, prior_probability, conditional_probability)
if (pred):
    print("Ad should go!")
else:
    print("Ad should not go!")
