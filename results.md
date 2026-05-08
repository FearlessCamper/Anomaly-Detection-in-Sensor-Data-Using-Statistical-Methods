# İstatistiksel Yöntemler ile Sensör Verilerinde Anomali Tespiti ve Veri İmputasyonu Karşılaştırması

Bu rapor, `AirQualityUCI.csv` veri seti üzerinde gerçekleştirilen Keşifçi Veri Analizi (EDA), Eksik Veri Tamamlama (Imputation) ve İstatistiksel Anomali Tespiti işlemlerinin sonuçlarını içermektedir.

## 1. Veri Ön İşleme ve İki Farklı Senaryo
Cihazların arıza verdiği anları temsil eden `-200` değerleri NaN (boşluk) yapılarak temizlenmiş ve %90'ı eksik olan `NMHC(GT)` sütunu projeden çıkarılmıştır. Analizin güvenirliğini test etmek için eksik veriler üzerinde iki farklı yaklaşım (senaryo) uygulanmıştır:

* **Senaryo 1 (Satırların Silinmesi):** İçinde eksik veri barındıran tüm satırlar düşürülmüştür. (Kalan boyut: 6941 satır)
* **Senaryo 2 (Ortalama ile Doldurma):** Eksik veriler, ait oldukları sütunun genel ortalaması hesaplanarak doldurulmuştur. Satır kaybı yaşanmamıştır. (Kalan boyut: 9357 satır)

---

## 2. Keşifçi Veri Analizi (EDA) Grafikleri
*(EDA grafikleri, verinin en saf hali olan Senaryo 1 veri seti üzerinden çizdirilmiştir.)*

### Sıcaklık (T) Dağılımı
Sıcaklık verilerinin genel dağılımını incelediğimizde, verinin çan eğrisine (normal dağılım) yakın bir profil çizdiği ancak sağa doğru hafif bir çarpıklık olduğu görülmektedir.
![Sıcaklık Dağılımı](temperature_distribution.png)

### Sıcaklık (T) ve Bağıl Nem (RH) İlişkisi
Sıcaklık ve bağıl nem arasındaki saçılım grafiği (scatter plot) incelendiğinde, sıcaklık arttıkça bağıl nem oranının düştüğünü gösteren belirgin bir negatif (ters) korelasyon göze çarpmaktadır.
![Sıcaklık ve Bağıl Nem İlişkisi](temperature_humidity_relationship.png)

### Karbonmonoksit (CO) Aykırı Değerleri
Karbonmonoksit değerleri bir kutu grafiği (boxplot) ile incelendiğinde; verilerin büyük çoğunluğunun normal seviyelerde (yeşil kutu içinde) toplandığı, ancak zaman zaman yüksek seviyelere fırlayan anlık ve tehlikeli artışların (aykırı değerlerin) yaşandığı tespit edilmiştir.
![Karbonmonoksit Aykırı Değerleri](co_outliers.png)

### Sensör Verileri Korelasyon Haritası
Farklı sensör ölçümleri arasındaki istatistiksel ilişkiyi gösteren ısı haritasına göre; `C6H6(GT)` ile diğer gaz sensörleri arasında güçlü pozitif korelasyonlar varken, `T` (Sıcaklık) ile `RH` (Bağıl Nem) arasında güçlü bir ters ilişki bulunmaktadır.
![Korelasyon Haritası](correlation_heatmap.png)

---

## 3. İstatistiksel Analiz ve Senaryo Karşılaştırması (Sıcaklık - 'T' Sütunu)

Eksik verileri silmenin (Senaryo 1) ve ortalama ile doldurmanın (Senaryo 2), dağılım parametrelerini ve anomali tespitini nasıl etkilediği aşağıda karşılaştırılmıştır:

### 3.1 Dağılım Parametreleri ve Normallik Kontrolü
| Metrik | Senaryo 1 (Silinmiş) | Senaryo 2 (Ort. ile Doldurulmuş) |
| :--- | :--- | :--- |
| **Ortalama ($\mu$)** | [Senaryo 1 Ortalama] | [Senaryo 2 Ortalama] |
| **Standart Sapma ($\sigma$)** | [Senaryo 1 Sapma] | [Senaryo 2 Sapma] |
| **68-95-99.7 (±1 Std)** | %[Senaryo 1 %1Std] | %[Senaryo 2 %1Std] |
| **68-95-99.7 (±2 Std)** | %[Senaryo 1 %2Std] | %[Senaryo 2 %2Std] |
| **Shapiro-Wilk P-Değeri**| [Senaryo 1 P Değeri] | [Senaryo 2 P Değeri] |
| **Normallik Sonucu** | H0 Reddedilir | H0 Reddedilir |

**Yorum:** Senaryo 2'de eksik değerlerin tamamı tek bir noktaya (ortalamaya) yığıldığı için standart sapmada daralma yaşanmış ve verinin yapay olarak merkezde sivrilmesine neden olmuştur. 

### 3.2 Q-Q Plot Karşılaştırması
*(Her iki senaryonun Q-Q plotları, dağılımın uç noktalarındaki sapmaları göstermektedir.)*
![Q-Q Plot (Senaryo 1)](qq_plot.png)
*(Buraya isterseniz Senaryo 2'nin Q-Q Plot resmini de ekleyebilirsiniz)*

### 3.3 Güven Aralıkları ve Anomali Tespiti ($|Z| > 3$)
| Metrik | Senaryo 1 (Silinmiş) | Senaryo 2 (Ort. ile Doldurulmuş) |
| :--- | :--- | :--- |
| **%95 Güven Aralığı** | ([Alt1], [Üst1]) | ([Alt2], [Üst2]) |
| **Tespit Edilen Anomali Sayısı**| [Senaryo 1 Anomali Sayısı] | [Senaryo 2 Anomali Sayısı] |

**Sonuç:** Eksik verilerin ortalama ile doldurulması (Senaryo 2), dağılımın yapısını ve standart sapmayı değiştirdiği için tespit edilen anomali (aykırı değer) miktarında farklılıklara yol açmıştır. Klasik istatistiksel anomali tespitinde, veri dağılımını suni olarak değiştiren doldurma yöntemleri yerine, temiz (silinmiş) veri seti (Senaryo 1) üzerinden ilerlemenin daha güvenilir olduğu sonucuna varılmıştır.
