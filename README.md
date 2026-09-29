                       EMLAK FİYAT TAHMİN VE KARAR DESTEK SİSTEMİ 

1. İş Problemi 

Gayrimenkul ilan platformumuzda satıcılar, evlerini listelerken piyasa değerini doğru belirleyememektedir. Bu durum evlerin aylarca satılamamasına (platformda ölü ilan kalabalığı oluşmasına) veya değerinin çok altında satılarak satıcıların maddi zarar etmesine yol açmaktadır. Temel amaç, sisteme yeni girilen bir evin piyasa değerini otomatik olarak hesaplayarak satıcılara veri odaklı bir "optimum fiyat önerisi" sunmaktır. 

2. Analiz Birimi 

Bu projede analiz birimi olarak ev ilanlarını ele alıyoruz. Yani tablodaki her bir satır house_id ile numaralandırılmış tek bir evi temsil ediyor. 

3. Hedef 

Evin fiziksel ve konumsal özelliklerini (büyüklük, bina yaşı, merkeze uzaklık, kalite skoru) girdi olarak kullanarak, price_index (fiyat endeksi) hedefini yüksek doğrulukla tahmin etmek. 

4. Zaman Ufku 

Geçmişte satılan evlerin verilerini kullanarak, yeni eklenecek bir evin fiyatını anlık olarak tahmin etmek. 

5. Başarı Metriği ve Baseline 

Başarı Metriği: Modelimizin ne kadar iyi çalıştığını MAE (Ortalama Mutlak Hata) ve R ²değerlerine bakarak ölçeceğiz. Amacımız, tahmin ettiğimiz price_index (fiyat) ile evin gerçek fiyatı arasındaki farkı (hatayı) en aza indirmek ve R²skorunu 0.75'in üzerine çıkarmaktır. 

Baseline: Evlerin özelliklerine hiç bakmadan, sistemdeki tüm evlerin ortalama fiyatını alıp eklenecek her eve bu ortalama fiyatı önerdiğimiz en basit "ortalama alma" yöntemidir. Kurduğumuz  modelin, bu basit yöntemden çok daha az hata yapmasını hedefliyoruz. 
 

6. Problemin Farklı Veri Madenciliği Görevleri Olarak Formüle Edilmesi 

Aynı veri setini kullanarak bu emlak problemini iki farklı mantıkla çözebiliriz: 

Görev 1: Regresyon Burada amacımız evin tam değerini bulmaktır. Evin metrekaresi (area_z), yaşı (age_z), merkeze uzaklığı (distance_center_z) ve kalitesi (quality_z) gibi özelliklerine bakarak, o evin fiyatını (price_index) doğrudan net bir sayı olarak (örneğin 542.47 veya 417.83 gibi) tahmin etmeye çalışıyoruz. 

Görev 2: Sınıflandırma Burada ise evlerin tam fiyatını bulmak yerine onları gruplara ayırıyoruz. Öncelikle evlerin price_index (fiyat) değerlerini kullanarak veriyi kategorize ediyoruz. Örneğin; değeri 450'den küçük olan evlere "Ekonomik", 450-520 arasında olanlara "Standart", 520'den büyük olanlara ise "Lüks" diyoruz. Ardından modelden tam bir fiyat söylemesini değil, özellikleri verilen evin hangi gruba (lüks mü, standart mı, ekonomik mi) ait olduğunu tahmin etmesini istiyoruz. 

7. Varsayımlar (Assumptions) 

Bu projeyi yaparken şu iki durumu doğru kabul ederek yola çıkıyoruz: 

Veriler zaten temizlenmiş: Tablodaki sütunların sonundaki _z harflerinden (area_z gibi) anladığımız kadarıyla, bu sayıların bizim için önceden matematiksel olarak düzenlendiğini ve modele verilmeye tam hazır hale getirildiğini varsayıyoruz.  

Ekonomi sabit: Gerçek hayatta ev fiyatlarını zıplatan enflasyon veya kriz gibi dış etkenlerin, tablomuzdaki fiyatları (price_index) tutarsız hale getirmediğini ve fiyatların dengeli olduğunu kabul ediyoruz. 

 

8. Sonuç  

 Bu veri madenciliği projesi sayesinde, geçmişteki emlak verilerini kazarak evin özellikleri ile fiyatı arasındaki gizli kuralları ortaya çıkarmış olacağız. Elde ettiğimiz bu veriye dayalı (data-driven) tahmin gücüyle satıcılara en mantıklı fiyatı önerecek ve yanlış fiyatlandırma yüzünden evlerin aylarca satılamaması sorununu çözeceğiz. 

 

 

 

 

 