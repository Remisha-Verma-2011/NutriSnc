import streamlit as st
from google import genai
import time  # 1. ADD THIS HERE at the top

# Set up your config
API_KEY = st.secrets["API_KEY"]
client = genai.Client(api_key=API_KEY)

st.set_page_config(page_title="NutriSync", page_icon="🍎")
st.title("🍎 NutriSync")

mode = st.selectbox("Choose your mode:", ["Kids", "Teens", "Adults"], key="unique_mode_select")

if prompt := st.chat_input("Ask NutriBuddy..."):
    st.write(f"User: {prompt}")
    
    try:
        # 2. ADD THE DELAY HERE, right before the request
        time.sleep(1) 
        
        # 3. USE THE MODEL NAME
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=f"You are a helpful nutrition assistant for {mode}. {prompt}"
        )
        st.write(f"NutriBuddy: {response.text}")
        
    except Exception as e:
        st.error("The AI is a bit busy right now. Please wait a second and try again!")