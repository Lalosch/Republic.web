import streamlit as st
from PIL import Image

st.set_page_config(page_title="La República", page_icon="🇷🇪", layout="centered")

st.title("La República")
st.markdown("Bienvenido a la web oficial de la Friends Republic. Navegá por nuestras instituciones, leyes y economía.")

st.image("bandera.jpeg", use_column_width=True)
st.markdown("## Secciones")
st.page_link("pages/1_Instituciones_publicas.py", label="Instituciones públicas")
st.page_link("pages/2_Politica.py", label="Política")
st.page_link("pages/3_Economia.py", label="Economía")
st.page_link("pages/4_Relaciones_internacionales.py", label="Relaciones internacionales/intercomisionales")
st.page_link("pages/5_Gobierno_y_funcionarios.py", label="Gobierno y funcionarios actuales")
st.page_link("pages/6_Consulta_PMR.py", label="Consultar tus PMR")