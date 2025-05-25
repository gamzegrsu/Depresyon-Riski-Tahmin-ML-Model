import streamlit as st
import numpy as np
import joblib
import random

# Model ve scaler yükle
model = joblib.load("logistic_model.pkl")
scaler = joblib.load("scaler.pkl")

# Kategori haritaları
cinsiyet_map = {"Erkek": 0, "Kadın": 1}
istah_map = {"Düşük": 0, "Orta": 1, "Yüksek": 2}
sigara_map = {"Hayır": 0, "Evet": 1}
alkol_map = {"Hayır": 0, "Evet": 1}

# Destekleyici moral mesajları
supportive_messages = [
    "Unutmayın, bu zor günler geçecek ve siz güçleneceksiniz. 🌈",
    "Kendinize karşı nazik olun; iyileşme zaman alır. 💖",
    "Her küçük adım, büyük değişimlerin başlangıcıdır. 👣",
    "Yanınızda destek olacak insanlar var, yalnız değilsiniz. 🤝",
    "Kendinizi sevin ve değer verin; buna her zaman değersiniz. 🌟",
    "Bugün yapabileceğiniz en iyi şey kendinize iyi bakmaktır. 🧘‍♀️",
    "Karanlık günlerin ardından her zaman güneş doğar. ☀️"
]

# Mental sağlık skoru açıklaması
st.markdown("""
# 🧠 Depresyon Riski Tahmin Uygulaması

### Mental Sağlık Skoru Nedir?

Mental sağlık skoru, kişinin genel ruh hali ve psikolojik durumunu gösteren bir ölçektir.  
Bu skor 0 ile 100 arasında değişir ve şu şekilde yorumlanabilir:

- **0 - 30:** Düşük mental sağlık, olası ciddi stres, depresyon ya da anksiyete belirtileri  
- **31 - 60:** Orta düzeyde mental sağlık, zaman zaman stres veya ruh hali dalgalanmaları olabilir  
- **61 - 100:** İyi mental sağlık, pozitif ruh hali ve psikolojik denge  

Lütfen kendi durumunuza en uygun skoru seçin.
---
""", unsafe_allow_html=True)

# Arka plan ve tema için CSS
st.markdown(
    """
    <style>
    /* Genel sayfa arka planı */
    .main {
        background: linear-gradient(135deg, #d1c4e9 0%, #ede7f6 100%);
        color: #1a237e;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }

    /* Başlık renk ve hizalama */
    h1, h2, h3 {
        color: #4a148c;
        text-align: center;
        font-weight: bold;
    }

    /* Slider ve input başlıkları */
    label {
        color: #4a148c !important;
        font-weight: bold !important;
    }

    /* Buton stilleri */
    div.stButton > button:first-child {
        background-color: #6a1b9a;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 10px 24px;
        transition: background-color 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #512da8;
        color: #fff;
    }

    /* Slider track renk */
    .stSlider > div[data-baseweb="slider"] > div {
        background: linear-gradient(90deg, #8e24aa 0%, #ce93d8 100%);
    }

    /* Slider üzerindeki numaralar (etiketler) */
    .stSlider span {
        background-color: black !important;
        color: white !important;
        padding: 2px 6px;
        border-radius: 6px;
        font-weight: bold;
    }

    /* Seçim kutuları */
    .stSelectbox > div > div {
        color: #4a148c;
        font-weight: bold;
    }

    /* Info ve error mesajları */
    .stAlert > div {
        border-radius: 10px;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sayfa başlığı
st.markdown("<h2>🧠 Depresyon Riski Tahmin Uygulaması</h2>", unsafe_allow_html=True)
st.markdown("---")

# Kullanıcı girdileri
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        yas = st.number_input("👶 Yaş", min_value=10, max_value=100, value=30)
        cinsiyet = st.selectbox("🚻 Cinsiyet", list(cinsiyet_map.keys()))
        uyku = st.slider("💤 Uyku Süresi (Saat)", 0.0, 12.0, 7.0)
        egzersiz = st.slider("🏃 Egzersiz Sıklığı (Hafta)", 0, 14, 3)
        ekran = st.slider("📱 Günlük Ekran Süresi (Saat)", 0.0, 24.0, 4.0)

    with col2:
        istah = st.selectbox("🍽️ İştah Seviyesi", list(istah_map.keys()))
        stres = st.slider("😰 Stres Seviyesi (1-10)", 1, 10, 5)
        nabiz = st.number_input("❤️ Nabız", min_value=40, max_value=200, value=70)
        sigara = st.selectbox("🚭 Sigara Kullanımı", list(sigara_map.keys()))
        alkol = st.selectbox("🍷 Alkol Tüketimi", list(alkol_map.keys()))
        mental_saglik = st.slider("🌟 Mental Sağlık Skoru (0-100)", 0, 100, 50)

st.markdown("---")

# Tahmin Butonu
if st.button("Tahmin Et 🧪"):
    stres_tersten = 11 - stres
    input_array = np.array([[yas,
                             cinsiyet_map[cinsiyet],
                             uyku,
                             egzersiz,
                             ekran,
                             istah_map[istah],
                             stres_tersten,
                             nabiz,
                             sigara_map[sigara],
                             alkol_map[alkol],
                             mental_saglik]])
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][prediction]

    if prediction == 1:
        st.error(f"⚠️ Yüksek depresyon riski. Tahmin güveni: %{prob*100:.2f}")
        mesaj = random.choice(supportive_messages)
        st.info(f"💬 Destek Mesajı: {mesaj}")
    else:
        st.success(f"✅ Düşük depresyon riski. Tahmin güveni: %{prob*100:.2f}")

