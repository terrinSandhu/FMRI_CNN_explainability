import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset from an Excel file
excel_file = "reducedata_bd1011.xlsx"  # Replace with the path to your Excel file
data = pd.read_excel(excel_file, engine="openpyxl")  # Make sure you have 'openpyxl' installed

# Assuming your dataset has columns 'X1', 'X2', ..., 'X80' for inputs and 'y' for the output
X = data.iloc[1:, 5:10]  # Features (inputs)
y = data.iloc[1:, 4]  # Target (output)

#print(y)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Create and train the Decision Tree model
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R²) Score: {r2}")

# Visualize the decision tree (optional)
from sklearn.tree import plot_tree
plt.figure(figsize=(12, 6))
plot_tree(model, feature_names=data.columns[:-1], filled=True, rounded=True, fontsize=10)
plt.show()
