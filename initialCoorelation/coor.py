import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset from an Excel file
excel_file = "reducedata_bd1011.xlsx"  # Replace with the path to your Excel file
df = pd.read_excel(excel_file, engine="openpyxl")  # Make sure you have 'openpyxl' installed


"""correlation_matrix = df.corr()  # df is your DataFrame
correlation_with_output = correlation_matrix['output'].abs()
correlated_features = correlation_with_output.sort_values(ascending=False)
print(correlated_features)"""

X = df.iloc[1:, 5:90]  # Features (inputs)
y = df.iloc[1:, 4]  # Target (output)

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(X, y)  # X is your input data, y is the output
feature_importance = model.feature_importances_
print(feature_importance)


from sklearn.feature_selection import mutual_info_regression
mi = mutual_info_regression(X, y)
print(mi)

import seaborn as sns
import matplotlib.pyplot as plt

correlation_matrix = df.corr()  # df is your DataFrame
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.show()


