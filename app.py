import streamlit as st
import pickle
import numpy as np

# --- 1. SETTINGS & STYLING ---
st.set_page_config(page_title="Indian Crop Analytics", page_icon="🌾", layout="centered")

# Custom Premium CSS for the "WOW" factor
st.markdown("""
    <style>
    .main {
        background-color: #0c1c0c;
        color: white;
    }
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                    url('https://images.unsplash.com/photo-1500382017468-9049fee74a62?auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
    }
    .stSelectbox, .stNumberInput {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    .prediction-box {
        background: rgba(70, 169, 8, 0.2);
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #66FF00;
        text-align: center;
        margin-top: 20px;
    }
    h1 {
        color: #66FF00 !important;
        text-align: center;
        font-family: 'Montserrat', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOAD AI MODEL ---
@st.cache_resource
def load_model():
    with open('crop_model_package.pkl', 'rb') as f:
        return pickle.load(f)

package = load_model()

# --- 3. THE WEBSITE UI ---
st.title("🌾 Indian Crop Production AI")
st.write("---")
st.write("Enter the farming details below to predict the production output.")

# Input Form
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        crop = st.selectbox("Select Crop Name", package['unique_crops'])
        state = st.selectbox("Select State", package['unique_states'])
    with col2:
        season = st.selectbox("Select Growing Season", package['unique_seasons'])
        cost = st.number_input("Cost of Cultivation (INR)", min_value=1000, value=15000, step=500)

    st.write("")
    if st.button("🚀 Predict Production Now"):
        # Encode inputs
        crop_enc = package['le_crop'].transform([crop])[0]
        state_enc = package['le_state'].transform([state])[0]
        season_enc = package['le_season'].transform([season])[0]
        
        # Predict
        input_data = np.array([[crop_enc, state_enc, season_enc, cost]])
        prediction = package['model'].predict(input_data)[0]
        
        # Display Result with Style
        st.markdown(f"""
            <div class="prediction-box">
                <h2 style="color: white; margin-bottom: 0;">Estimated Production</h2>
                <h1 style="font-size: 50px; margin-top: 10px;">{prediction:.2f} Units</h1>
                <p style="opacity: 0.7;">Prediction based on regional agricultural trends</p>
            </div>
            """, unsafe_allow_html=True)

st.write("---")
st.caption("Developed by Antigravity AI | Empowering Farmers through Data")

