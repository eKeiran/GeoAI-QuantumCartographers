import streamlit as st

st.set_page_config(
    page_title="GeoAI Reimagined",
    page_icon="📊",
    layout="wide",
)

st.title("GeoAI Reimagined: Transformative and Diverse Earth Science Applications Using Foundation Models.")

# Button to show the file uploader
if st.button('Click to Upload Image'):
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
        st.write("Image successfully uploaded!")
