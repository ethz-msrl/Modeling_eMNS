import numpy as np
import os
import math
from sklearn.preprocessing import MinMaxScaler
import pickle


def load_data_forGridSearch(path, dataset_type):
    """
    Load training and testing dataset.
    Split data into features and labels.
    :param path: data file path
    :param dataset_type: type of dataset, "train" or "test"
    :return: feature and label numpy array depending on dataset_type
    """

    data = np.load(os.path.join(path, "{}.npy".format(dataset_type)))

    feature = data[:, :-3]
    label = data[:, -3:]

    assert feature.shape[1] == 11, "Imported features do not have the correct dimension"
    assert label.shape[1] == 3, "Imported labels do not have the correct dimension"

    return feature, label


def feature_scaling_forGridSearch(train, test):
    """
    Perform feature scaling based on the entire training dataset, and also apply it to the testing dataset.
    :param train: numpy array of training features
    :param test: numpy array of testing features
    :return: scaled numpy array of training and testing features, based on the max. and min. value in the training set
    """
    minmax_scale = MinMaxScaler().fit(train)
    train_transformed = minmax_scale.transform(train)
    test_transformed = minmax_scale.transform(test)

    assert train.shape == train_transformed.shape, "Feature dimension for the training set is changed due to scaling"
    assert test.shape == test_transformed.shape, "Feature dimension for the testing set is changed due to scaling"
    assert np.max(train_transformed) <= 1 + math.exp(-9), "The max. value of the training feature exceeds 1"
    assert np.min(train_transformed) >= 0, "The min. value of the training feature belows 0"

    return train_transformed, test_transformed


def save_object(obj, filename, foldername = "./GridSearchResults"):
    if not os.path.exists(foldername):
        os.makedirs(foldername)

    with open(os.path.join(foldername, filename), 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


# used to load grid search object
def load_object(filename):
    return pickle.load(open(filename, 'rb'))


