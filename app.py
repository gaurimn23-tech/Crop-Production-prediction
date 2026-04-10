import streamlit as st
import os
import pickle

st.set_page_config(page_title="System Check")

st.title("🔍 Website Diagnostic Tool")

# 1. Show all files to find the missing one
st.subheader("Files found on the server:")
files = os.listdir('.')
st.write(files)

# 2. Check for the specific file
file_name = 'crop_model_package.pkl'
if file_name in files:
    st.success(f"✅ Found it! The file '{file_name}' exists.")
    
    # Try to load it
    try:
        with open(file_name, 'rb') as f:
            data = pickle.load(f)
        st.success("🧠 Brain loaded successfully! You can now use the normal code.")
    except Exception as e:
        st.error(f"❌ Found the file, but couldn't open it: {e}")
else:
    st.error(f"⚠️ Missing! I cannot see '{file_name}' anywhere in the list above.")
    
st.info("💡 If you see the file in the list above but with a different name (like 'Crop_model...'), let me know!")

