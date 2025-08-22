import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Price Compare App",
    page_icon="🛍️",
    layout="wide"
)

st.title("🛍️ AI-Powered Price Comparison")
st.write("Upload a product image to find the best deals!")

# Placeholder for image upload
uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=200)
