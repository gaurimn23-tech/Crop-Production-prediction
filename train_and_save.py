import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# 1. Create/Load Sample Data
data = {
    'Crop': ['Rice', 'Wheat', 'Maize', 'Cotton', 'Sugarcane', 'Rice', 'Wheat', 'Maize', 'Cotton', 'Sugarcane'],
    'State': ['Punjab', 'Haryana', 'UP', 'Gujarat', 'Maharashtra', 'Haryana', 'Punjab', 'Gujarat', 'Maharashtra', 'UP'],
    'Season': ['Kharif', 'Rabi', 'Kharif', 'Kharif', 'Whole Year', 'Kharif', 'Rabi', 'Kharif', 'Kharif', 'Whole Year'],
    'Cost_of_Cultivation': [15000, 12000, 10000, 18000, 25000, 15500, 12500, 10500, 18500, 25500],
    'Production': [4500, 3800, 2500, 5000, 8000, 4600, 3900, 2600, 5100, 8100]
}
df = pd.DataFrame(data)

# 2. Initialize Encoders
le_crop = LabelEncoder()
le_state = LabelEncoder()
le_season = LabelEncoder()

# 3. Transform Data
df['Crop'] = le_crop.fit_transform(df['Crop'])
df['State'] = le_state.fit_transform(df['State'])
df['Season'] = le_season.fit_transform(df['Season'])

# 4. Train Model
X = df[['Crop', 'State', 'Season', 'Cost_of_Cultivation']]
y = df['Production']
model = LinearRegression()
model.fit(X, y)

# 5. SAVE EVERYTHING
save_data = {
    "model": model,
    "le_crop": le_crop,
    "le_state": le_state,
    "le_season": le_season,
    "unique_crops": list(le_crop.classes_),
    "unique_states": list(le_state.classes_),
    "unique_seasons": list(le_season.classes_)
}

with open('crop_model_package.pkl', 'wb') as f:
    pickle.dump(save_data, f)

print("Saved model and encoders successfully to 'crop_model_package.pkl'")
