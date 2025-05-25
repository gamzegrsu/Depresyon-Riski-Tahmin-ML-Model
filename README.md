# Depresyon-Riski-Tahmin-ML-Model

📌 Proje Hakkında
Bu proje, bireylerin ruh sağlığıyla ilgili çeşitli yaşam alışkanlıklarını analiz ederek depresyon riski taşıyıp taşımadıklarını tahmin eden bir makine öğrenimi modelini kapsamaktadır. Projede lojistik regresyon algoritması ile sınıflandırma yapılmıştır.

Veriler kullanıcının uyku süresi, stres seviyesi, alkol/sigara kullanımı gibi parametrelere göre değerlendirilmekte ve bireyin depresyon riski olup olmadığı tahmin edilmektedir.

🧪 Kullanılan Algoritma: Lojistik Regresyon
Neden Lojistik Regresyon?
İkili sınıflandırma problemleri için uygundur (0 = düşük risk, 1 = yüksek risk).

Yorumlanabilirliği yüksek, sade ve etkili bir modeldir.

Özellikle dengeli veya büyük veri setlerinde güvenilir sonuçlar verir.

📊 Model Performansı
Başarı Skoru:
Accuracy (Doğruluk): 0.85004

Sınıflandırma Raporu:
Sınıf	Precision	Recall	F1-Score	Support
0 (Düşük Risk)	0.76	0.68	0.72	14063
1 (Yüksek Risk)	0.88	0.92	0.90	35937
Toplam				50000

Not: Proje aşamasında test amacıyla farklı veri bölünmeleriyle modelin doğruluğu 1.00 seviyesine kadar çıkarılmıştır. Bu durum, veri sızıntısı veya aşırı öğrenme ihtimaline karşı dikkatle değerlendirilmiştir.

🎯 Çözümlediği Problem
Bu proje, bireylerin yaşam alışkanlıklarına göre depresyon risklerini hızlı ve otomatik şekilde değerlendirmeyi hedefler. Klinik tanıların öncesinde bireylerin farkındalık kazanmasına yardımcı olur.

🌍 Gerçek Hayatta Kullanım Senaryoları
Psikolojik Destek Platformları: Kullanıcıların kendi mental sağlık durumlarını değerlendirmelerine yardımcı olur.

Mobil Sağlık Uygulamaları: Egzersiz, uyku ve stres takibi yapan uygulamalara entegre edilebilir.

Kurumsal Refah Programları: Çalışanların ruhsal durumlarını gözlemleyerek destek planlaması yapılabilir.

🧱 Veri Özellikleri
Aşağıdaki değişkenler modele giriş olarak kullanılmıştır:

Yaş

Cinsiyet

Uyku süresi

Egzersiz sıklığı

Günlük ekran süresi

İştah seviyesi

Stres seviyesi

Nabız

Sigara ve alkol kullanımı

Mental sağlık skoru

Mental Sağlık Skoru Açıklaması:

0 - 30: Düşük mental sağlık – ciddi stres, depresyon veya anksiyete belirtileri

31 - 60: Orta düzey – zaman zaman ruh hali dalgalanmaları

61 - 100: İyi mental sağlık – pozitif ruh hali ve denge

🔄 Gelecekte Nasıl Geliştirilebilir?
📈 Model Seçimi Genişletilebilir: Random Forest, XGBoost gibi daha güçlü algoritmalarla karşılaştırmalı analiz yapılabilir.

📊 Gerçek Zamanlı Veri Kullanımı: Giyilebilir cihazlardan gelen anlık verilerle canlı tahmin sistemleri kurulabilir.

🧠 Psikolojik Test Entegrasyonu: Beck depresyon envanteri gibi testlerle desteklenebilir.

🗣️ Doğal Dil İşleme (NLP): Kullanıcıların yazılı ifadelerinden duygu analizi yapılabilir.


KAGGLE LİNK = https://www.kaggle.com/models/gamzegrsu/depresyon-tahmin-model
