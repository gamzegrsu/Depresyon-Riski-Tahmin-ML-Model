import streamlit as st
import joblib
import numpy as np

# Model ve scaler dosyaları aynı klasörde olmalı
model = joblib.load("logistic_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Depresyon Riski Tahmin Sistemi")

# Kullanıcıdan özellikleri alıyoruz
yas = st.number_input("Yaş", min_value=18, max_value=70, value=30)
cinsiyet = st.selectbox("Cinsiyet", ["Erkek", "Kadın", "Diğer"])
uyku = st.slider("Uyku Süresi (Saat)", 0.0, 12.0, 6.5)
egzersiz = st.number_input("Haftalık Egzersiz Sıklığı", 0, 14, 3)
ekran = st.slider("Günlük Ekran Süresi (Saat)", 0.0, 16.0, 6.0)
istah = st.selectbox("İştah Seviyesi", ["Az", "Normal", "Çok"])
stres = st.slider("Stres Seviyesi (1-10)", 1, 10, 5)
nabiz = st.number_input("Nabız", 40, 120, 70)
sigara = st.selectbox("Sigara Kullanımı", ["Evet", "Hayır"])
alkol = st.selectbox("Alkol Tüketimi", ["Hiç", "Az", "Orta", "Fazla"])

# Label encoding eşlemeleri (eğitimle aynı olmalı)
cinsiyet_map = {"Erkek": 0, "Kadın": 1, "Diğer": 2}
istah_map = {"Az": 0, "Normal": 1, "Çok": 2}
sigara_map = {"Hayır": 0, "Evet": 1}
alkol_map = {"Hiç": 0, "Az": 1, "Orta": 2, "Fazla": 3}

# Girdi verisini numpy array olarak hazırla
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
    alkol_map[alkol]
]])

# Ölçekle
input_scaled = scaler.transform(input_array)

# Tahmin ve sonuç gösterme
if st.button("Tahmin Et"):
    prediction = model.predict(input_scaled)[0]
    if prediction == 1:
        st.success("Depresyon Riski VAR.")
    else:
        st.success("Depresyon Riski YOK.")
