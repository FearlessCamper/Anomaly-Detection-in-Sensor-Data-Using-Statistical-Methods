import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv("C:\\Users\\USER\\Documents\\pythonProject\\istatistik\\AirQualityUCI.csv",sep=';',decimal=',')  # Veriyi yükleme
data = data.dropna(how='all', axis=1)#fazlalık sütunları kaldırma 
data = data.dropna(how='all', axis=0)#

# Verideki tüm -200'leri ve -200.0'leri bulup NaN (boşluk) ile değiştiriyoruz
data = data.replace(-200, np.nan)#-200 değerleri sensör hatası veya eksik veri olarak kabul edilir, bu yüzden NaN ile değiştiriyoruz

print(data.columns)  # Veri setindeki sütun adlarını görüntüleme
#'Date', 'Time', 'CO(GT)', 'PT08.S1(CO)', 'NMHC(GT)', 'C6H6(GT)','PT08.S2(NMHC)', 'NOx(GT)', 'PT08.S3(NOx)', 'NO2(GT)', 'PT08.S4(NO2)','PT08.S5(O3)', 'T', 'RH', 'AH', #--> silindi 'Unnamed: 15', 'Unnamed: 16'

# temel veri keşfi (EDA) için bazı temel komutlar:
print(data.head())# Verinin ilk 5 satırına bakmak için (genel yapıyı görmek için çok faydalıdır)
print(data.shape)# Veri setinin satır ve sütun sayısını (boyutunu) öğrenmek için
print(data.info())# Sütun isimleri, veri tipleri (int, float, object vb.) ve eksik veri (null) olup olmadığını görmek için
print(data.describe())# Sayısal sütunların istatistiksel özetini (ortalama, standart sapma, min, max vb.) almak için
print(data.isnull().sum())# Hangi sütunda kaç tane eksik (NaN/Null) değer olduğunu bulmak için

# Veri görselleştirme için 4 farklı grafik oluşturalım:
# figsize ile pencerenin genel boyutunu (genişlik, yükseklik) ayarlıyoruz
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 12))

# --- 1. GRAFİK (Sol Üst) ---
sns.histplot(data['T'], kde=True, bins=30, color='blue', ax=axes[0, 0])
axes[0, 0].set_title('Sıcaklık (T) Dağılımı')
axes[0, 0].set_xlabel('Sıcaklık')

# --- 2. GRAFİK (Sağ Üst) ---
sns.scatterplot(x='T', y='RH', data=data, alpha=0.5, color='orange', ax=axes[0, 1])
axes[0, 1].set_title('Sıcaklık (T) ve Bağıl Nem (RH) İlişkisi')
axes[0, 1].set_xlabel('Sıcaklık')
axes[0, 1].set_ylabel('Bağıl Nem')

# --- 3. GRAFİK (Sol Alt) ---
# Farklılık olsun diye Karbonmonoksit için bir Kutu Grafiği (Aykırı Değer) ekleyelim
sns.boxplot(x=data['CO(GT)'], color='green', ax=axes[1, 0])
axes[1, 0].set_title('Karbonmonoksit (CO) Aykırı Değerleri')
axes[1, 0].set_xlabel('CO(GT)')

# --- 4. GRAFİK (Sağ Alt) ---
# Korelasyon Isı Haritası
sensor_verileri = data[['CO(GT)', 'NMHC(GT)', 'C6H6(GT)', 'NOx(GT)', 'NO2(GT)', 'T', 'RH']]
korelasyon = sensor_verileri.corr()
sns.heatmap(korelasyon, annot=True, cmap='viridis', fmt=".2f", ax=axes[1, 1])
axes[1, 1].set_title('Sensör Verileri Korelasyon Haritası')

# Yazıların ve grafiklerin birbirine girmesini engellemek için sihirli dokunuş:
plt.tight_layout()
# Tüm tabloyu tek seferde göster!
plt.show()

#################################################################################
print("\n###############################################################################")
# 1. ADIM: İşe yaramaz sütunu veri setinden tamamen atıyoruz
data = data.drop(columns=['NMHC(GT)'])

# (Opsiyonel) Tarih ve Saat şu an modelleme için metin formatında, 
# sayısal modeller hata vermesin diye şimdilik onları da çıkarabiliriz:
data_sayisal = data.drop(columns=['Date', 'Time'])

# ---------------------------------------------------------
# SENARYO 1: Eksik Satırları Silerek (Temiz Veri)
# ---------------------------------------------------------
data_silinmis = data_sayisal.dropna()
print("\n1. Senaryo (Satırlar Silindi) Boyutu:", data_silinmis.shape)

# ---------------------------------------------------------
# SENARYO 2: Ortalama ile Doldurarak 
# ---------------------------------------------------------
data_ortalama = data_sayisal.copy()

for sutun in data_ortalama.columns:
    sutun_ortalamasi = data_ortalama[sutun].mean()
    data_ortalama[sutun] = data_ortalama[sutun].fillna(sutun_ortalamasi)
    
print("2. Senaryo (Ortalama ile Dolduruldu) Eksik Sayısı:", data_ortalama.isnull().sum().sum())

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# İşlem yapacağımız sütunu seçiyoruz (Örnek: Sıcaklık - 'T')
secilen_kolon = 'T'
veri = data_silinmis[secilen_kolon]

#############################################################

# ==========================================
# 1. PARAMETRE TAHMİNİ (μ, σ)
# ==========================================
mu = veri.mean()
sigma = veri.std()
print("1. PARAMETRE TAHMİNİ")
print(f"Ortalama (μ): {mu:.4f}")
print(f"Standart Sapma (σ): {sigma:.4f}\n")

# ==========================================
# 2. Z-SKORU HESAPLAMA
# ==========================================
# Veri setimize yeni bir sütun olarak Z-skorlarını ekliyoruz
data_silinmis['Z_Skoru'] = (veri - mu) / sigma
print("2. Z-SKORU HESAPLANDI (Veri setine 'Z_Skoru' sütunu eklendi)\n")

# ==========================================
# 3. 68-95-99.7 KURALI KONTROLÜ
# ==========================================
oran_1_std = len(veri[(data_silinmis['Z_Skoru'] >= -1) & (data_silinmis['Z_Skoru'] <= 1)]) / len(veri) * 100
oran_2_std = len(veri[(data_silinmis['Z_Skoru'] >= -2) & (data_silinmis['Z_Skoru'] <= 2)]) / len(veri) * 100
oran_3_std = len(veri[(data_silinmis['Z_Skoru'] >= -3) & (data_silinmis['Z_Skoru'] <= 3)]) / len(veri) * 100

print("3. 68-95-99.7 KURALI KONTROLÜ")
print(f"±1 Standart Sapma içindeki veri oranı (Beklenen ~%68): %{oran_1_std:.2f}")
print(f"±2 Standart Sapma içindeki veri oranı (Beklenen ~%95): %{oran_2_std:.2f}")
print(f"±3 Standart Sapma içindeki veri oranı (Beklenen ~%99.7): %{oran_3_std:.2f}\n")

# ==========================================
# 4. NORMALLİK TESTLERİ
# ==========================================
print("4. NORMALLİK TESTLERİ")
# Shapiro-Wilk Testi
# Uyarı: SciPy shapiro testi 5000'den büyük N için P-değerinde hatalı olabilir.
stat, p_value = stats.shapiro(veri)
print(f"Shapiro-Wilk Test İstatistiği: {stat:.4f}, p-değeri: {p_value:.4e}")
if p_value > 0.05:
    print("Sonuç: Veri normal dağılıma uyuyor (H0 reddedilemez).")
else:
    print("Sonuç: Veri normal dağılıma uymuyor (H0 reddedilir).")

# Q-Q Plot Çizimi
plt.figure(figsize=(8, 5))
stats.probplot(veri, dist="norm", plot=plt)
plt.title(f"{secilen_kolon} Sütunu için Q-Q Plot")
plt.show()
print("\n")

# ==========================================
# 5. ANOMALİ TESPİTİ (|Z| > 3)
# ==========================================
# Mutlak değeri 3'ten büyük olan Z-skorlarını filtreliyoruz
anomaliler = data_silinmis[abs(data_silinmis['Z_Skoru']) > 3]

print("5. ANOMALİ TESPİTİ (|Z| > 3)")
print(f"Toplam tespit edilen anomali sayısı: {len(anomaliler)}")
if len(anomaliler) > 0:
    print("Örnek Anomaliler:")
    print(anomaliler[[secilen_kolon, 'Z_Skoru']].head())
print("\n")

# ==========================================
# 6. GÜVEN ARALIKLARI (%95)
# ==========================================
# %95 Güven Aralığı (Popülasyon ortalaması için)
n = len(veri)
standart_hata = sigma / np.sqrt(n)
alt_sinir, ust_sinir = stats.norm.interval(0.95, loc=mu, scale=standart_hata)

print("6. GÜVEN ARALIKLARI (%95)")
print(f"Ortalama için %95 Güven Aralığı: ({alt_sinir:.4f},  {ust_sinir:.4f})")