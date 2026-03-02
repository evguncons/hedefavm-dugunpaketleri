import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# 1. Streamlit sayfa ayarlarını yapılandır
st.set_page_config(
    page_title="HedefAVM Dijital Katalog",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Gereksiz Streamlit boşluklarını sıfırlama, Header/Footer (Manage App) Gizleme
st.markdown("""
    <style>
        /* Streamlit varsayılan üst menü, header ve footer gizleme */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        [data-testid="stHeader"] {display: none;}
        [data-testid="stToolbar"] {display: none;}
        
        /* Tam ekran için tüm boşlukları sıfırlama */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        
        .stApp {
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden !important;
        }
        
        /* Katalog iframe'ini tam ekran yapma */
        iframe {
            height: 100vh !important;
            border: none !important;
            display: block;
        }
    </style>
""", unsafe_allow_html=True)

# 2. Dosya yolları (Aynı klasörde oldukları varsayılmaktadır)
pdf_file_path = "dugunpaketi2026.pdf"
html_file_path = "index.html"

# 3. PDF ve HTML dosyalarını oku
if not os.path.exists(pdf_file_path):
    st.error(f"⚠️ Hata: '{pdf_file_path}' dosyası bulunamadı. Lütfen PDF dosyasını uygulamanın yanına koyun.")
    st.stop()

if not os.path.exists(html_file_path):
    st.error(f"⚠️ Hata: '{html_file_path}' dosyası bulunamadı. Lütfen index.html dosyasını uygulamanın yanına koyun.")
    st.stop()

# PDF'i Base64 formatına çevir (Streamlit iframe'i dış dosyaları güvenlikten dolayı engelleyebileceği için veriyi direkt HTML'e gömüyoruz)
with open(pdf_file_path, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_data_uri = f"data:application/pdf;base64,{base64_pdf}"

# HTML'i metin olarak oku
with open(html_file_path, "r", encoding="utf-8") as f:
    html_code = f.read()

# 4. HTML içindeki varsayılan dosya adını, kodlanmış Base64 verimiz ile değiştir
html_code = html_code.replace(
    "let DEFAULT_PDF_URL = 'dugunpaketi2026.pdf';", 
    f"let DEFAULT_PDF_URL = '{pdf_data_uri}';"
)

# 5. HTML (Katalog) bileşenini Streamlit ekranına bas
# CSS ile 100vh verdiğimiz için height değerinin iframe üzerinde responsive olmasını sağladık
components.html(html_code, height=1000, scrolling=False)
