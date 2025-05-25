import streamlit as st
import numpy as np
import joblib

# Model ve scaler yükle
model = joblib.load("logistic_model.pkl")
scaler = joblib.load("scaler.pkl")

# Kategori değişkenler için haritalar
cinsiyet_map = {"Erkek": 0, "Kadın": 1}
istah_map = {"Düşük": 0, "Orta": 1, "Yüksek": 2}
sigara_map = {"Hayır": 0, "Evet": 1}
alkol_map = {"Hayır": 0, "Evet": 1}

st.title("Depresyon Riski Tahmini")

# Kullanıcı girdileri
yas = st.number_input("Yaş", min_value=10, max_value=100, value=30)
cinsiyet = st.selectbox("Cinsiyet", list(cinsiyet_map.keys()))
uyku = st.slider("Uyku Süresi (Saat)", 0.0, 12.0, 7.0)
egzersiz = st.slider("Egzersiz Sıklığı (Hafta)", 0, 14, 3)
ekran = st.slider("Günlük Ekran Süresi (Saat)", 0.0, 24.0, 4.0)
istah = st.selectbox("İştah Seviyesi", list(istah_map.keys()))
stres = st.slider("Stres Seviyesi (1-10)", 1, 10, 5)
nabiz = st.number_input("Nabız", min_value=40, max_value=200, value=70)
sigara = st.selectbox("Sigara Kullanımı", list(sigara_map.keys()))
alkol = st.selectbox("Alkol Tüketimi", list(alkol_map.keys()))

st.subheader("Mental Sağlık Anketi (Son 1 hafta)")

# Anket soruları - 1 ile 5 arasında puanlama (1=Hiç, 5=Çok sık)
soru1 = st.slider("1. Kendinizi ne kadar mutlu hissettiniz?", 1, 5, 3)
soru2 = st.slider("2. Ne kadar stresli hissettiniz?", 1, 5, 3)
soru3 = st.slider("3. Uyku kaliteniz nasıldı?", 1, 5, 3)
soru4 = st.slider("4. Enerji seviyeniz nasıldı?", 1, 5, 3)
soru5 = st.slider("5. Sosyal ilişkilerinizden ne kadar memnunsunuz?", 1, 5, 3)

# Basit puan hesaplama: tüm soruların ortalaması, mental sağlık skoru olarak kullanacağız
mental_saglik = (soru1 + (6 - soru2) + soru3 + soru4 + soru5) / 5 * 20  # 20 ile çarparak 0-100 arası yapıyoruz

# (Not: Stres sorusunu ters puanladık çünkü yüksek stres düşük mental sağlık demek)

if st.button("Tahmin Et"):
    input_array = np.array([[
        yas,
        cinsiyet_map[cinsiyet],
        uyku,
        egzersiz,
        ekran,
        istah_map[istah],
        stres,
        nabiz,
        sigara_map[sigara],
        alkol_map[alkol],
        mental_saglik
    ]])

    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][prediction]

    if prediction == 1:
        st.error(f"Yüksek depresyon riski. Tahmin güveni: %{prob*100:.2f}")
    else:
        st.success(f"Düşük depresyon riski. Tahmin güveni: %{prob*100:.2f}")
