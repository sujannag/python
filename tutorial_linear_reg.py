import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split

# import the data
from sklearn.datasets import load_boston

# load the data into a variable
boston = load_boston()

# Create a dataframe from the loaded data
df_x = pd.DataFrame(boston.data, columns = boston.feature_names)    # probably the data to be trained
df_y = pd.DataFrame(boston.target)                                  # Target data is also mapped

# Shows a lot of parameters regarding the data
#print(df_x.values)
# df_x.to_csv('df_x.csv')
# df_y.to_csv('df_y.csv')

# get an object for the linear regression model
reg = linear_model.LinearRegression()

# split the data into training and testing data. The training data is set at 80% and the test
# data is set at 20%, the data is sorted randomly.
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size = 0.2, random_state = 4)

# For visualization only
# x_train.to_csv('x_train.csv')
# x_test.to_csv('x_test.csv')
# y_train.to_csv('y_train.csv')
# y_test.to_csv('y_test.csv')

# do the fitting/training of the data
reg.fit(x_train, y_train, sample_weight = None)

# gets the coeffitients, dont know what they are used for anyways
# print(reg.coef_)

# Prediction of Data
x_predict = reg.predict(x_test)

#print(x_predict, y_test)

# calculate error using root mean square
print(np.mean((x_predict - y_test)**2))