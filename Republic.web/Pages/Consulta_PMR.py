import streamlit as st
from PIL import Image
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

st.set_page_config(page_title="Consulta de PMR", page_icon="🔎")

try:
    image = Image.open("bandera.jpeg")
    st.image(image, width=200)
except:
    st.markdown("<h4 style='color:gray;'>[Bandera no encontrada]</h4>", unsafe_allow_html=True)

st.markdown("""
    <div style='background-color:#4bb5f5;padding:10px;border-radius:10px;margin-bottom:20px;'>
        <h1 style='color:#f6c542;text-align:center;'>Consulta de tus PMR</h1>
    </div>
""", unsafe_allow_html=True)

st.write("Ingresá tu código personal para consultar tus PMR:")

codigo_ingresado = st.text_input("Código")

if codigo_ingresado:
    try:
        # lee las credenciales
        creds = Credentials.from_service_account_file(
            'pmr-salarios-0d934e33ea2e.json',
            scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']
        )
        client = gspread.authorize(creds)

        # abre la hoja
        sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1kJwSvQ7F9udNxAmkianHMRIexcihsCyY4ax07KnJFJw/edit")
        worksheet = sheet.sheet1
        data = worksheet.get_all_records()
        df = pd.DataFrame(data)

        # busca el código
        usuario = df[df['codigo'].astype(str) == codigo_ingresado.strip()]

        if not usuario.empty:
            nombre = usuario.iloc[0]['nombre']
            numero = usuario.iloc[0]['numero']
            pmr = usuario.iloc[0]['pmr']
            st.success(f"**Nombre:** {nombre}\n\n**Número:** {numero}\n\n**PMR:** {pmr}")
        else:
            st.error("Código no encontrado.")
    except Exception as e:
        st.error(f"Ocurrió un error: {e}")
    