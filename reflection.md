# PROJE ÖZELEŞTİRİSİ VE RİSK ANALİZİ
Kurulan emlak fiyat tahmin modelinin gerçek hayatta yanlış sonuçlar üretebileceği iki temel risk ve bunlara karşı alınması gereken önlemler aşağıda belirtilmiştir:

### Risk 1: Ekonomik Değişimler ve Enflasyon Etkisi
Emlak piyasasında fiyatlar sabit değildir; enflasyon, faiz oranları veya dönemsel krizlerle hızla değişebilir. Modelimiz geçmiş döneme ait verilerle eğitildiği için, bugünün ekonomik şartlarını (örneğin ani bir enflasyon artışını) hesaba katmayıp yeni girilen bir eve piyasanın çok altında, komik bir fiyat tahmini yapabilir.

**Alınan Önlem: Bu riski minimize etmek için fiyatların ham hali yerine enflasyondan arındırılmış bir "fiyat endeksi" (price_index) kullanılmıştır. Ancak kalıcı çözüm olarak modele "Satış Tarihi" ve "Güncel Kredi Faizi" gibi zaman serisi değişkenleri eklenmelidir.


### Risk 2: Aykırı Değerlerin (Outliers) Modeli Yanıltması
Veri setinde standart evlerin yanı sıra, istisnai özelliklere sahip aşırı pahalı yalılar veya çok ucuz harabe evler bulunabilir. Model bu uç noktalardaki (aykırı) evlerin özelliklerini ezberlemeye çalışırsa, normal bir apartman dairesinin fiyatını da gereksiz yere yüksek veya düşük tahmin ederek sapabilir.

**Alınan Önlem: Modelin kafasının karışmasını engellemek için, veriler model eğitimine sokulmadan önce Z-Skoru standardizasyonu (_z uzantılı veriler) ile ölçeklendirilmiştir. Bu sayede verilerdeki aşırı uçurumlar istatistiksel olarak törpülenmiştir
