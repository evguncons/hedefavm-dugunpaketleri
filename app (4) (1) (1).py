import streamlit as st
import streamlit.components.v1 as components
import base64
import os
import re

st.set_page_config(page_title="HEDEF AVM - BAYRAM ETTİREN FIRSATLAR KATALOG", layout="wide", initial_sidebar_state="collapsed")

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

# --- DİKKAT: BİLGİSAYARDAN VEYA SUNUCUDAN OKUNACAK PDF ADI BURADA ---
pdf_file_path = "dugunpaketi2026.pdf"
html_file_path = "index.html"

# Dosya Kontrolleri
if not os.path.exists(pdf_file_path):
    st.error(f"⚠️ Hata: '{pdf_file_path}' bulunamadı. Lütfen PDF dosyasının app.py ile aynı klasörde yan yana olduğundan emin olun.")
    st.stop()
    
if not os.path.exists(html_file_path):
    st.error(f"⚠️ Hata: '{html_file_path}' bulunamadı. Lütfen HTML dosyasının app.py ile aynı klasörde yan yana olduğundan emin olun.")
    st.stop()

# PDF'i Base64'e Çevirme
with open(pdf_file_path, "rb") as f:
    pdf_data_uri = f"data:application/pdf;base64,{base64.b64encode(f.read()).decode('utf-8')}"

# HTML'i okuma
with open(html_file_path, "r", encoding="utf-8") as f:
    html_code = f.read()

# Düzenli İfade (Regex) ile index.html içindeki PDF adını (ne olduğu fark etmeksizin) otomatik bul ve Base64 verisi ile değiştir
html_code = re.sub(r"let\s+DEFAULT_PDF_URL\s*=\s*'[^']+';", f"let DEFAULT_PDF_URL = '{pdf_data_uri}';", html_code)

# İframe'i oluştur
components.html(html_code)
