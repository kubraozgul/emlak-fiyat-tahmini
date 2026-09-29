import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Klasör Hazırlığı
# Hocanın istediği 'figures' klasörünü otomatik oluşturuyoruz
os.makedirs('figures', exist_ok=True)

# 2. Veriyi Yükleme ve Temizleme
# Daha önce SQL'de yaptığımız mantıklı filtrelemenin aynısını burada da yapıyoruz
df = pd.read_csv('housing_regression.csv')
df = df.dropna(subset=['price_index'])
df = df[df['price_index'] > 0]

# 3. Bağımsız (Girdi) ve Bağımlı (Hedef) Değişkenleri Ayırma
# 'house_id' model için bir özellik olmadığından (sadece sıra numarası olduğu için) almıyoruz
X = df[['area_z', 'age_z', 'distance_center_z', 'quality_z']]
y = df['price_index']

# 4. Modeli Eğitmek İçin Veriyi Bölme (%80 Eğitim, %20 Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Modeli Eğitme (Regresyon Görevi)
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Tahmin ve Başarı Ölçümü
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# 7. Sonuçları 'results.csv' Dosyasına Kaydetme
results_df = pd.DataFrame({
    'Metrik': ['Ortalama Mutlak Hata (MAE)', 'R-Kare (R2)'],
    'Skor': [round(mae, 2), round(r2, 4)]
})
results_df.to_csv('results.csv', index=False)

# 8. Görselleştirme 1: Gerçek ve Tahmin Edilen Fiyatların Karşılaştırması
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.5, color='blue')
# Kusursuz tahmin çizgisini (kırmızı kesik çizgi) çiziyoruz
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Gerçek Fiyat Endeksi')
plt.ylabel('Tahmin Edilen Fiyat Endeksi')
plt.title('Gerçek vs. Tahmin Edilen Ev Fiyatları')
plt.savefig('figures/gercek_vs_tahmin.png') # Resmi klasöre kaydet
plt.close()

# 9. Görselleştirme 2: Ev Büyüklüğü ile Fiyat Arasındaki İlişki
plt.figure(figsize=(8, 6))
plt.scatter(df['area_z'], df['price_index'], alpha=0.5, color='green')
plt.xlabel('Ev Büyüklüğü (area_z)')
plt.ylabel('Fiyat Endeksi (price_index)')
plt.title('Ev Büyüklüğü Arttıkça Fiyat Nasıl Değişiyor?')
plt.savefig('figures/buyukluk_ve_fiyat.png') # Resmi klasöre kaydet
plt.close()

print("Model başarıyla çalıştı! 'results.csv' dosyası ve 'figures' klasörü oluşturuldu.")