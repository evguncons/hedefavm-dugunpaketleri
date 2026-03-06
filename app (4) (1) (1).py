import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(page_title="HedefAVM Dijital Katalog", layout="wide", initial_sidebar_state="collapsed")

# AÇILIŞTA GÖRÜNEN TURUNCU EKRANI KALDIRAN VE YENİ TEMAYA UYAN CSS
st.markdown("""
    <style>
        /* Streamlit Menüleri Gizle */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Arkaplanı yeni Lüks Temaya (Mürdüm/Magenta) sabitle */
        .stApp, .main {
            background-color: #830642 !important;
            background-image: linear-gradient(135deg, #c71a6c 0%, #830642 100%) !important;
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden !important;
        }
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        
        /* Iframe Kapsayıcısını ve İframe'in Kendisini Ekranın Tamamına Zorla */
        [data-testid="stHtml"], iframe {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            height: 100dvh !important;
            border: none !important;
            z-index: 99999 !important;
            background-color: transparent !important;
        }
    </style>
""", unsafe_allow_html=True)

# 2. Dosya Yolları
pdf_file_path = "dugunpaketi2026.pdf"
html_file_path = "index.html"

# Dosya Kontrolleri ve Base64'e Çevirme
if not os.path.exists(pdf_file_path) or not os.path.exists(html_file_path):
    st.error("Lütfen PDF ve HTML dosyalarının yan yana olduğundan emin olun.")
    st.stop()

with open(pdf_file_path, "rb") as f:
    pdf_data_uri = f"data:application/pdf;base64,{base64.b64encode(f.read()).decode('utf-8')}"

with open(html_file_path, "r", encoding="utf-8") as f:
    html_code = f.read().replace("let DEFAULT_PDF_URL = 'dugunpaketi2026.pdf';", f"let DEFAULT_PDF_URL = '{pdf_data_uri}';")

# 3. İframe'i oluştur
components.html(html_code)
