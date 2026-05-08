# İstatistiksel Yöntemler ile Hava Kalitesi Analizi ve Anomali Tespiti

Bu proje, Hava Kalitesi (Air Quality) veri seti üzerinde klasik istatistiksel yöntemler kullanarak Keşifçi Veri Analizi (EDA) yapmak ve eksik veri işleme yöntemlerinin (Data Imputation) anomali tespiti üzerindeki etkilerini karşılaştırmak amacıyla geliştirilmiştir.

## 📋 Proje Özeti ve Metodoloji

Proje kapsamında, sensör verilerindeki cihaz hataları (`-200` değerleri) temizlendikten sonra analiz süreci iki farklı senaryo üzerinden yürütülmüştür:

1.  **Senaryo 1 (Satır Silme - Dropna):** Eksik veri içeren satırlar veri setinden tamamen çıkarılmıştır. Bu yöntem, veri kaybına yol açsa da mevcut verinin doğal dağılımını korur.
2.  **Senaryo 2 (Ortalama ile Doldurma - Imputation):** Eksik veriler, ait oldukları sütunun ortalaması ile doldurulmuştur. Bu yöntem veri bütünlüğünü korur ancak istatistiksel varyansı (sapmayı) yapay olarak düşürebilir.

Her iki senaryo için şu analizler yapılmıştır:
- **Normal Dağılım Tahmini:** Ortalama ($\mu$) ve Standart Sapma ($\sigma$) hesaplaması.
- **Z-Skoru ve 68-95-99.7 Kuralı:** Verinin teorik dağılıma uyumu.
- **Normallik Testleri:** Shapiro-Wilk testi ve Q-Q Plot görselleştirmesi.
- **Anomali Tespiti:** $|Z| > 3$ koşulunu sağlayan aykırı değerlerin belirlenmesi.
- **Güven Aralıkları:** %95 olasılıkla popülasyon parametre tahmini.

## ⚙️ Gereksinimler

Projenin çalışması için **Python 3.8+** gereklidir. Gerekli kütüphaneler:
- `pandas`, `numpy`, `scipy`, `matplotlib`, `seaborn`

## 🚀 Kurulum ve Kullanım

```bash
# 1. Kütüphaneleri kurun
pip install -r requirements.txt

# 2. Betiği çalıştırın
python proje_kodu.py
```

---

## 📊 Analiz Görselleri (EDA)

Analiz süreci, verinin ham yapısını anlamak için Senaryo 1 (Temiz Veri) üzerinden aşağıdaki görselleştirmelerle desteklenmiştir:

| Dağılım Analizi | İlişki Analizi |
| :--- | :--- |
| ![Sıcaklık Dağılımı](temperature_distribution.png) | ![Sıcaklık ve Nem İlişkisi](temperature_humidity_relationship.png) |

| Aykırı Değerler (Boxplot) | Korelasyon Isı Haritası |
| :--- | :--- |
| ![CO Aykırı Değerler](co_outliers.png) | ![Isı Haritası](correlation_heatmap.png) |

---

## 📈 Sonuçların Karşılaştırılması

### Normallik ve Q-Q Plot
Verilerin normal dağılım çizgisine uyumu her iki senaryo için test edilmiştir. Aşağıdaki grafik, verinin kuyruklardaki sapmasını göstermektedir:
![Q-Q Plot](qq_plot.png)

### İstatistiksel Çıkarım
Analiz sonucunda, eksik verileri **ortalama ile doldurmanın (Senaryo 2)**, standart sapmayı yapay olarak daralttığı ve verinin merkezde sivrilmesine neden olduğu gözlemlenmiştir. Bu durum, anomali tespit eşiklerini değiştirerek farklı sonuçlar doğurmaktadır. Klasik istatistiksel analizlerde, veri dağılımını bozmamak adına **Senaryo 1 (Silme)** yönteminin daha güvenilir olduğu sonucuna varılmıştır.
