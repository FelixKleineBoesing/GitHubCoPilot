# read txt file "pima-indians-diabetes.txt" from data folder into variable data as dataframe
import pandas as pd

data = pd.read_csv("data/pima-indians-diabetes.txt", header=None)

# print column names of the variable data
print(data.columns)

# create correlation heatmap for all numerical values of data
import seaborn as sns



# One hot encode all categorical variables of data


# split data in train and test data


# oversample the 1 class in the test set


# train an XGBoostClassifier with 20 iterations


# function that return feature importances based on a supplied XGBoostClassifier model