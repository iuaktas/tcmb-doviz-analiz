
# TCMB Döviz Kurları Veri Çekme ve Görselleştirme

Bu Python projesi, Türkiye Cumhuriyet Merkez Bankası'nın (TCMB) yayınladığı günlük döviz kurlarını otomatik olarak indirip, kaydeder ve seçili para birimleri için temel bir grafik hazırlar.

---

## 🚀 Özellikler

- TCMB API'sinden döviz verilerini çeker.  
- Verileri `CSV` formatında kaydeder.  
- USD, EUR, GBP alış kurlarını bar grafik şeklinde görselleştirir.

---

## 💻 Kullanım

1. Gerekli kütüphaneleri yükleyin:

```
pip install -r requirements.txt
```

2. Scripti çalıştırın:

```
python tcmb_doviz_analiz.py
```

---

## 📊 Kaydedilen Dosya

Çalıştırıldığında veriler, scriptin çalıştığı dizine aşağıdaki isimle kaydedilir:

```
tcmb_doviz_kurlari_YYYY-MM-DD.csv
```

---

## 🔗 Veri Kaynağı

TCMB Resmi XML Döviz Kurları:  
https://www.tcmb.gov.tr/kurlar/today.xml

---

## 📌 Gereksinimler

- Python 3.8+
- requests
- pandas
- matplotlib

---

## 🤝 Katkı

Proje geliştirilmeye açıktır! İsteyen herkes fork edip katkıda bulunabilir.
