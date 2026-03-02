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

# SİYAH BOŞLUK SORUNUNU ÇÖZEN STREAMLIT CSS AYARLARI
st.markdown("""
    <style>
        /* Gereksiz Streamlit menülerini gizle */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        [data-testid="stHeader"] {display: none;}
        [data-testid="stToolbar"] {display: none;}
        
        /* Streamlit'in kendi siyah arkaplanını gizlemek için ana rengi değiştiriyoruz */
        .stApp, .main {
            background-color: #f70059 !important;
            background-image: linear-gradient(135deg, #f70059 0%, #ff4d15 100%) !important;
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden !important;
        }
        
        .block-container {
            padding: 0rem !important;
            margin: 0rem !important;
            max-width: 100% !important;
        }
        
        /* Iframe'i mobil ekrana %100 kilitleyen, siyah boşlukları engelleyen kod */
        iframe {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            height: 100dvh !important; /* Mobil tarayıcılar için dinamik yükseklik */
            border: none !important;
            z-index: 999999 !important;
            background-color: transparent !important;
        }
    </style>
""", unsafe_allow_html=True)

# 2. Dosya yolları
pdf_file_path = "dugunpaketi2026.pdf"
html_file_path = "index.html"

# 3. Dosyaları kontrol et
if not os.path.exists(pdf_file_path):
    st.error(f"⚠️ Hata: '{pdf_file_path}' dosyası bulunamadı. Lütfen PDF dosyasını uygulamanın yanına koyun.")
    st.stop()

if not os.path.exists(html_file_path):
    st.error(f"⚠️ Hata: '{html_file_path}' dosyası bulunamadı. Lütfen index.html dosyasını uygulamanın yanına koyun.")
    st.stop()

# 4. PDF'i Base64 formatına çevir
with open(pdf_file_path, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_data_uri = f"data:application/pdf;base64,{base64_pdf}"

# 5. HTML'i metin olarak oku
with open(html_file_path, "r", encoding="utf-8") as f:
    html_code = f.read()

# HTML içindeki varsayılan dosya adını Base64 verimiz ile değiştir
html_code = html_code.replace(
    "let DEFAULT_PDF_URL = 'dugunpaketi2026.pdf';", 
    f"let DEFAULT_PDF_URL = '{pdf_data_uri}';"
)

# 6. HTML bileşenini ekrana bas
# CSS ile 'position: fixed' ve '100dvh' verdiğimiz için height parametresini kaldırarak tam ekran esnekliği sağladık.
components.html(html_code)
