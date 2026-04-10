import streamlit as st
import pickle
import numpy as np

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Crop Predictor India", page_icon="🌾", layout="centered")

# --- CUSTOM CSS FOR PREMIUM GLASSMORHISM LOOK ---
st.markdown("""
    <style>
    .main {
        background-image: url('https://images.unsplash.com/photo-1500382017468-9049fee74a62?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
    }
    .stApp {
        background: rgba(0, 0, 0, 0.5); /* Dark overlay */
    }
    .css-1r6slb0, .stForm {
        background: rgba(255, 255, 255, 0.15) !important;
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 20px;
        padding: 30px;
        color: white;
    }
    h1 {
        color: #66FF00 !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    .stButton>button {
        background-color: #46A908 !important;
        color: white !important;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOAD THE MODEL ---
@st.cache_resource
def load_model():
    try:
        with open('crop_model_package.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None

package = load_model()

if package:
    st.title("🌾 Indian Crop Production Predictor")
    st.write("Professional AI-Powered Agriculture Analytics")

    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        with col1:
            crop = st.selectbox("Select Crop", package['unique_crops'])
            state = st.selectbox("Select State", package['unique_states'])
        with col2:
            season = st.selectbox("Select Season", package['unique_seasons'])
            cost = st.number_input("Cost of Cultivation (INR)", min_value=1000, value=15000)
        
        submit = st.form_submit_button("Predict Production")

    if submit:
        # Encode inputs
        crop_enc = package['le_crop'].transform([crop])[0]
        state_enc = package['le_state'].transform([state])[0]
        season_enc = package['le_season'].transform([season])[0]
        
        # Predict
        pred = package['model'].predict(np.array([[crop_enc, state_enc, season_enc, cost]]))[0]
        
        st.success(f"### Estimated Production: {pred:.2f} Units")
else:
    st.error("Error: 'crop_model_package.pkl' not found. Please upload it to GitHub!")
