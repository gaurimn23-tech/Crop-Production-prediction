# -------------------------------------------------------------------
# Project: Prediction of Agriculture Crop Production in India
# Author: Antigravity AI
# Description: A beginner-friendly Machine Learning project using Linear Regression.
# -------------------------------------------------------------------

# STEP 1: IMPORTING LIBRARIES
# ---------------------------------------------------------
# We import libraries to use their special functions.
import pandas as pd              # Used for data handling (tables)
import numpy as np               # Used for mathematical operations
import matplotlib.pyplot as plt  # Used for creating graphs/plots
from sklearn.model_selection import train_test_split # To split data into Training and Testing
from sklearn.linear_model import LinearRegression    # The Machine Learning model we will use
from sklearn.preprocessing import LabelEncoder       # To convert text data into numbers
from sklearn.metrics import mean_squared_error       # To check how accurate our model is

print("Step 1: Libraries imported successfully!\n")

# STEP 2: CREATING A SAMPLE DATASET (CSV FILE)
# ---------------------------------------------------------
# Since we don't have a dataset yet, we will create one ourselves.
# In a real project, you would skip this and use pd.read_csv('your_file.csv').

data = {
    'Crop': ['Rice', 'Wheat', 'Maize', 'Cotton', 'Sugarcane', 'Rice', 'Wheat', 'Maize', 'Cotton', 'Sugarcane'],
    'State': ['Punjab', 'Haryana', 'UP', 'Gujarat', 'Maharashtra', 'Haryana', 'Punjab', 'Gujarat', 'Maharashtra', 'UP'],
    'Season': ['Kharif', 'Rabi', 'Kharif', 'Kharif', 'Whole Year', 'Kharif', 'Rabi', 'Kharif', 'Kharif', 'Whole Year'],
    'Cost_of_Cultivation': [15000, 12000, 10000, 18000, 25000, 15500, 12500, 10500, 18500, 25500],
    'Production': [4500, 3800, 2500, 5000, 8000, 4600, 3900, 2600, 5100, 8100]
}

df_sample = pd.DataFrame(data)
df_sample.to_csv('agriculture_data.csv', index=False)
print("Step 2: Sample dataset 'agriculture_data.csv' created and saved!\n")

# STEP 3: LOADING THE DATASET
# ---------------------------------------------------------
# Load the CSV file into a pandas DataFrame.
df = pd.read_csv('agriculture_data.csv')

# Display first 5 rows
print("--- First 5 rows of the dataset ---")
print(df.head())
print("\n")

# STEP 4: HANDLING MISSING VALUES
# ---------------------------------------------------------
# Check if there are any empty cells.
print("Checking for missing values:")
print(df.isnull().sum())

# If there were missing values, we could fill them with the mean (average):
# df['Production'] = df['Production'].fillna(df['Production'].mean())
print("No missing values found in our sample data.\n")

# STEP 5: CONVERTING CATEGORICAL DATA INTO NUMBERS
# ---------------------------------------------------------
# Computers only understand numbers. Labels like 'Rice' need to be 0, 1, 2...
le = LabelEncoder()

df['Crop'] = le.fit_transform(df['Crop'])
df['State'] = le.fit_transform(df['State'])
df['Season'] = le.fit_transform(df['Season'])

print("--- Data after converting text to numbers ---")
print(df.head())
print("\n")

# STEP 6: SPLITTING DATA INTO TRAINING AND TESTING SETS
# ---------------------------------------------------------
# We use 'X' for input features and 'y' for what we want to predict (Production).
X = df[['Crop', 'State', 'Season', 'Cost_of_Cultivation']]
y = df['Production']

# Split: 80% for training the model, 20% for testing it.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Total rows: {len(df)}")
print(f"Training rows: {len(X_train)}")
print(f"Testing rows: {len(X_test)}\n")

# STEP 7: TRAINING THE LINEAR REGRESSION MODEL
# ---------------------------------------------------------
# Initialize the model
model = LinearRegression()

# Train the model using the training data
model.fit(X_train, y_train)
print("Step 7: Model Training Complete!\n")

# STEP 8: MAKING PREDICTIONS
# ---------------------------------------------------------
# Ask the model to predict values for the test set.
y_pred = model.predict(X_test)

# Compare Actual vs Predicted
comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("--- Comparison: Actual vs Predicted ---")
print(comparison)
print("\n")

# STEP 9: VISUALIZATION (GRAPHS)
# ---------------------------------------------------------
plt.figure(figsize=(10,6))

# Plotting Actual vs Predicted values
plt.scatter(y_test, y_pred, color='blue', label='Predictions')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linewidth=2, label='Perfect Fit')

plt.title('Actual vs Predicted Crop Production')
plt.xlabel('Actual Production')
plt.ylabel('Predicted Production')
plt.legend()
plt.grid(True)
plt.show()

print("Step 9: Graph displayed successfully!\n")

# STEP 10: MANUAL PREDICTION (EXAMPLE INPUT)
# ---------------------------------------------------------
# Let's predict for a new case: Crop=0, State=1, Season=2, Cost=20000
new_data = [[0, 1, 2, 20000]] 
prediction = model.predict(new_data)
print(f"Example Prediction for input {new_data}: {prediction[0]:.2f}")

# STEP 11: HOW TO SAVE THE MODEL (OPTIONAL)
# ---------------------------------------------------------
import pickle
with open('crop_model.pkl', 'wb') as file:
    pickle.dump(model, file)
print("\nStep 11: Model saved as 'crop_model.pkl'")
