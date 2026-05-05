# İstatistiksel Yöntemler ile Sensör Verilerinde Anomali Tespiti

Bu proje, Hava Kalitesi (Air Quality) veri seti üzerinde klasik istatistiksel yöntemler kullanılarak Keşifçi Veri Analizi (EDA) ve Tek Değişkenli Anomali Tespiti (Univariate Anomaly Detection) yapılması amacıyla geliştirilmiştir.

## 📋 Proje Açıklaması

Bir hava kalitesi izleme cihazından alınan saatlik sensör verileri (Sıcaklık, Karbonmonoksit vb.) incelenmiştir. Veri setindeki cihaz hataları (`-200` değerleri) temizlenmiş, aşırı eksik veri içeren sütunlar (`NMHC(GT)`) çıkarılmış ve kalan temiz veri üzerinde şu istatistiksel analizler uygulanmıştır:

- **Normal Dağılım Parametre Tahmini:** Ortalama (μ) ve Standart Sapma (σ) hesaplaması.
- **Z-Skoru Dönüşümü:** Verilerin standart normal dağılıma uyarlanması.
- **68-95-99.7 Kuralı (Empirik Kural):** Veri dağılımının teorik normal dağılıma uygunluğunun kontrolü.
- **Normallik Testleri:** Shapiro-Wilk istatistiksel testi ve Q-Q Plot görselleştirmesi.
- **Anomali Tespiti:** Z-Skoru mutlak değerce 3'ten büyük olan (`|Z| > 3`) aykırı değerlerin (anomalilerin) tespit edilmesi.
- **Güven Aralıkları:** Popülasyon ortalaması için %95 güven aralığının hesaplanması.

## ⚙️ Gereksinimler

Projenin sorunsuz çalışması için sisteminizde **Python 3.8 veya üzeri** bir sürümün yüklü olması gerekmektedir. Kullanılan temel kütüphaneler şunlardır:
- `pandas` (Veri manipülasyonu)
- `numpy` (Sayısal işlemler)
- `scipy` (İstatistiksel testler ve hesaplamalar)
- `matplotlib` & `seaborn` (Veri görselleştirme)

## 🚀 Kurulum ve Çalıştırma

**Adım 1:** Gerekli kütüphaneleri bilgisayarınıza kurun. Terminal veya komut satırını açıp proje dizininde şu komutu çalıştırın:
```bash
pip install -r requirements.txt