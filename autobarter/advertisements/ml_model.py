import pandas as pd
import matplotlib.pyplot as plt
import pickle

#df = pd.read_csv("autobarter.csv")
df = pd.read_csv("autobarter_elantra.csv")

df["foreign/ghana"].unique()

from sklearn.preprocessing import LabelEncoder
le_fg = LabelEncoder()
df['foreign/ghana'] = le_fg.fit_transform(df['foreign/ghana'])
df["foreign/ghana"].unique()

le_model = LabelEncoder()
df['model'] = le_model.fit_transform(df['model'])
df["model"].unique()

le_make = LabelEncoder()
df['make'] = le_make.fit_transform(df['make'])
df["make"].unique()

le_body_type = LabelEncoder()
df['body_type'] = le_body_type.fit_transform(df['body_type'])
df["body_type"].unique()

le_transmission = LabelEncoder()
df['transmission'] = le_transmission.fit_transform(df['transmission'])
df["transmission"].unique()

le_fuel_type = LabelEncoder()
df['fuel_type'] = le_fuel_type.fit_transform(df['fuel_type'])
df["fuel_type"].unique()

le_trim_edition = LabelEncoder()
df['trim/edition'] = le_trim_edition.fit_transform(df['trim/edition'])
df["trim/edition"].unique()

le_location = LabelEncoder()
df['location'] = le_location.fit_transform(df['location'])
df["location"].unique()

le_registered = LabelEncoder()
df['registered'] = le_registered.fit_transform(df['registered'])
df["registered"].unique()

X = df.drop(["title","market_value"], axis=1)
y = df["market_value"]

from sklearn.linear_model import LinearRegression
linear_reg = LinearRegression()
linear_reg.fit(X, y.values)

from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
error = np.sqrt(mean_squared_error(y, y_pred))

from sklearn.tree import DecisionTreeRegressor
dec_tree_reg = DecisionTreeRegressor(random_state=0)
dec_tree_reg.fit(X, y.values)

y_pred = dec_tree_reg.predict(X)

error = np.sqrt(mean_squared_error(y, y_pred))

from sklearn.ensemble import RandomForestRegressor
random_forest_reg = RandomForestRegressor(random_state=0)
random_forest_reg.fit(X, y.values)

y_pred = random_forest_reg.predict(X)

error = np.sqrt(mean_squared_error(y, y_pred))
print("¢{:,.02f}".format(error))

from sklearn.model_selection import GridSearchCV

max_depth = [None, 2,4,6,8,10,12]
parameters = {"max_depth": max_depth}

regressor = DecisionTreeRegressor(random_state=0)
gs = GridSearchCV(regressor, parameters, scoring='neg_mean_squared_error')
gs.fit(X.values, y.values)

regressor = gs.best_estimator_

regressor.fit(X.values, y.values)
y_pred = regressor.predict(X)
error = np.sqrt(mean_squared_error(y, y_pred))
print("¢{:,.02f}".format(error))


with open('saved_steps.pkl', 'rb') as file:
    data = pickle.load(file)

regressor_loaded = data["model"]
le_fg = data["le_fg"]
le_model = data["le_model"]
le_make = data["le_make"]
le_body_type = data["le_body_type"]
le_transmission = data["le_transmission"]
le_location = data["le_location"]
le_registered = data["le_registered"]
le_fuel_type = data["le_fuel_type"]
le_trim_edition = data["le_trim_edition"]
mileage = data["mileage"]
engine_capacity = data["engine_capacity"]
registration_year = data["registration_year"]
year_of_manufacture = data["year_of_manufacture"]
