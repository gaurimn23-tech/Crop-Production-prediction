from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# --- LOAD THE MODEL ---
def load_model():
    try:
        with open('crop_model_package.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None

package = load_model()

@app.route('/')
def home():
    if not package:
        return "Error: Model file 'crop_model_package.pkl' not found. Please run 'train_and_save.py' first."
    
    # Send lists to the HTML for dropdowns
    data = {
        "crops": package['unique_crops'],
        "states": package['unique_states'],
        "seasons": package['unique_seasons']
    }
    return render_template('index.html', data=data)

@app.route('/predict', methods=['POST'])
def predict():
    if not package:
        return jsonify({"error": "Model not loaded"}), 500
    
    try:
        # Get data from the form (sent as JSON via JavaScript)
        input_data = request.json
        
        # 1. Convert text inputs back to numbers using saved Encoders
        crop_encoded = package['le_crop'].transform([input_data['crop']])[0]
        state_encoded = package['le_state'].transform([input_data['state']])[0]
        season_encoded = package['le_season'].transform([input_data['season']])[0]
        cost = float(input_data['cost'])
        
        # 2. Prepare data for model
        input_array = np.array([[crop_encoded, state_encoded, season_encoded, cost]])
        
        # 3. Predict
        prediction = package['model'].predict(input_array)[0]
        
        return jsonify({"prediction": round(prediction, 2)})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
