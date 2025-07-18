import streamlit as st
from PIL import Image

st.set_page_config(page_title="Economía", page_icon="💰")

try:
image = Image.open("bandera.jpeg")
st.image(image, width=200)
except:
st.markdown("<h4 style='color:gray;'>[Bandera no encontrada]</h4>", unsafe_allow_html=True)

st.markdown("""
<div style='background-color:#4bb5f5;padding:10px;border-radius:10px;margin-bottom:20px;'>
<h1 style='color:#f6c542;text-align:center;'>Economía</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("Sistema monetario, contratos laborales, gremios y más...")