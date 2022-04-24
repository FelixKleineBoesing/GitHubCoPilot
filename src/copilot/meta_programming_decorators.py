import pandas as pd
import seaborn as sns

# log beginning and end of every function in this module with a decorator
import logging


def log_function_entry_exit(func):
    """
    Log the beginning and end of every function in this module with a decorator.
    """
    logging.info('Entering function {}'.format(func.__name__))
    result = func()
    logging.info('Exiting function {}'.format(func.__name__))
    return result


@log_function_entry_exit
def read_csv(file_path):
    """
    Reads a CSV file and log the beginning and end of the function.
    """
    df = pd.read_csv(file_path)
    return df


@log_function_entry_exit
def create_correlation_visualization(df):
    """
    Creates a correlation matrix of the given dataframe
    and generates a heatmap visualization

    :param df: The dataframe.
    :type df: pandas.DataFrame
    :return: The correlation visualization.
    :rtype: str
    """
    corr = df.corr()
    return sns.heatmap(corr, annot=True)


@log_function_entry_exit
def fit_model_on_train_data(model, X_train, y_train):
    """
    Fits a model on the training data.

    :param model: The model.
    :type model: sklearn.model
    :param X_train: The training data.
    :type X_train: numpy.array
    :param y_train: The training labels.
    :type y_train: numpy.array
    :return: The fitted model.
    :rtype: sklearn.model
    """
    return model.fit(X_train, y_train)


def evaluate_predictions(model, X_test, y_test):
    """
    Evaluates the predictions of a model.

    :param model: The model.
    :type model: sklearn.model
    :param X_test: The test data.
    :type X_test: numpy.array
    :param y_test: The test labels.
    :type y_test: numpy.array
    :return: The evaluation metrics.
    :rtype: dict
    """
    return model.evaluate(X_test, y_test)