import numpy as np


def binary_classification_metrics(y_pred, y_true):
    """
    Computes metrics for binary classification
    Arguments:
    y_pred, np array (num_samples) - model predictions
    y_true, np array (num_samples) - true labels
    Returns:
    precision, recall, f1, accuracy - classification metrics
    """

    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score

    true_positive = ((y_pred == 1) & (y_true == 1)).sum()
    true_negative = ((y_pred == 0) & (y_true == 0)).sum()
    false_negative = ((y_pred == 0) & (y_true == 1)).sum()
    false_positive = ((y_pred == 1) & (y_true == 0)).sum()

    if true_positive == 0:
        precision = 0
        recall = 0
        f1 = 0
    else:
        precision = true_positive / (true_positive + false_positive)
        recall = true_positive / (true_positive + false_negative)
        f1 = 2 * precision * recall / (precision + recall)
    accuracy = (true_positive + true_negative) / len(y_true)

    return precision, recall, f1, accuracy


def multiclass_accuracy(y_pred, y_true):
    """
    Computes metrics for multiclass classification
    Arguments:
    y_pred, np array of int (num_samples) - model predictions
    y_true, np array of int (num_samples) - true labels
    Returns:
    accuracy - ratio of accurate predictions to total samples
    """

    accuracy = (y_true == y_pred).sum() / len(y_true)
    return accuracy


def r_squared(y_pred, y_true):
    """
    Computes r-squared for regression
    Arguments:
    y_pred, np array of int (num_samples) - model predictions
    y_true, np array of int (num_samples) - true values
    Returns:
    r2 - r-squared value
    """
    y_mean = y_true.mean()
    r2 = 1 - (sum((y_pred - y_true) ** 2))/(sum((y_true - y_mean) ** 2))
    return r2


def mse(y_pred, y_true):
    """
    Computes mean squared error
    Arguments:
    y_pred, np array of int (num_samples) - model predictions
    y_true, np array of int (num_samples) - true values
    Returns:
    mse - mean squared error
    """

    mean_squared_error = sum((y_pred - y_true) ** 2) / len(y_true)
    return mean_squared_error


def mae(y_pred, y_true):
    """
    Computes mean absolut error
    Arguments:
    y_pred, np array of int (num_samples) - model predictions
    y_true, np array of int (num_samples) - true values
    Returns:
    mae - mean absolut error
    """

    mean_absolute_error = sum(np.absolute(y_pred - y_true)) / len(y_true)
    return mean_absolute_error