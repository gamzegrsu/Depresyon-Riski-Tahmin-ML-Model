import streamlit as st
import numpy as np
import joblib

# Model ve scaler'ı yükle
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Sayfa yapılandırması
st.set_page_config(page_title="Depresyon Riski Tahmini", layout="centered")

# Özel mor tema ve eğlenceli CSS
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #6a0dad 0%, #9c27b0 100%);
        color: white;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }

    h1, h2, h3 {
        color: #e1bee7;
        text-align: center;
        font-weight: bold;
    }

    label {
        color: #e1bee7 !important;
        font-weight: bold !important;
    }

    div.stButton > button:first-child {
        background-color: #ab47bc;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 10px 24px;
        transition: background-color 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #8e24aa;
        color: #fff;
    }

    .stSlider > div[data-baseweb="slider"] > div {
        background: linear-gradient(90deg, #ab47bc 0%, #ce93d8 100%);
    }

    .stSelectbox > div > div {
        color: #e1bee7;
        font-weight: bold;
    }

    .stAlert > div {
        border-radius: 10px;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Bilgilendirici başlık
st.markdown("""
## 🌈 Mental Sağlık Skoru Rehberi:

- **80-100** → Zihinsel sağlık çok iyi 💪
- **60-79** → Ortalama – küçük stresler olabilir 🧘‍♀️
- **40-59** → Dikkat edilmeli – stres ve yorgunluk artmış olabilir 😕
- **0-39** → Zihinsel sağlık zayıf – destek önerilir ❤️‍🩹
""")

# Başlık
st.title("💜 Depresyon Riski Tahmin Uygulaması")

# Girdi alanları
yas = st.slider("Yaş", 10, 100, 30)
cinsiyet = st.selectbox("Cinsiyet", ["Kadın", "Erkek"])
uyku = st.slider("Günlük Uyku Süresi (saat)", 0, 12, 7)
egzersiz = st.slider("Haftalık Egzersiz Sıklığı", 0, 14, 3)
ekran = st.slider("Günlük Ekran Süresi (saat)", 0, 16, 6)
istah = st.slider("İştah Seviyesi (1-10)", 1, 10, 5)
stres = st.slider("Stres Seviyesi (1-10)", 1, 10, 5)
nabiz = st.slider("Nabız", 40, 120, 75)
sigara = st.selectbox("Sigara Kullanımı", ["Evet", "Hayır"])
alkol = st.selectbox("Alkol Tüketimi", ["Evet", "Hayır"])
mental = st.slider("Mental Sağlık Skoru (0-100)", 0, 100, 50)

# Dönüştürmeler
cinsiyet_bin = 1 if cinsiyet == "Kadın" else 0
sigara_bin = 1 if sigara == "Evet" else 0
alkol_bin = 1 if alkol == "Evet" else 0

# Tahmin yap
if st.button("💡 Tahmin Et"):
    input_array = np.array([[yas, cinsiyet_bin, uyku, egzersiz, ekran, istah, stres,
                             nabiz, sigara_bin, alkol_bin, mental]])
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        st.error("⚠️ Yüksek depresyon riski tespit edildi.")
        st.markdown("💌 *Unutma, yalnız değilsin. İyi hissetmek zaman alabilir ama bu süreci birlikte aşabiliriz.*")
    else:
        st.success("🎉 Düşük depresyon riski! Harika gidiyorsun.")
        st.markdown("🌼 *Kendine iyi bakmaya devam et, sen harikasın!*")

