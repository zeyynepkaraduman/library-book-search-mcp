<<<<<<< HEAD
# Kütüphane Kitap Arama MCP

Bu MCP (Model Context Protocol) servisi, Google Books API kullanarak kitap arama işlevselliği sağlar. Smithery platformunda deploy edilebilir ve çeşitli AI uygulamalarıyla entegre edilebilir.

## Özellikler

- 📚 **Genel Kitap Arama**: Kitap adı, yazar veya konuya göre arama
- 👤 **Yazara Göre Arama**: Belirli bir yazarın tüm kitaplarını bulma
- 🏷️ **Kategoriye Göre Arama**: Belirli kategorilerdeki kitapları listeleme
- 📖 **Detaylı Kitap Bilgisi**: Kitap ID'si ile tam kitap detaylarını alma
- 🌍 **Çoklu Dil Desteği**: Türkçe, İngilizce ve diğer dillerde arama
- ⚡ **Hızlı Yanıt**: Google Books API ile optimize edilmiş sorgular

## Kullanılabilir Araçlar

### 1. search_library_books
Genel kitap arama işlevi.

**Parametreler:**
- `query` (string): Aranacak kitap, yazar veya konu
- `max_results` (int, opsiyonel): Maksimum sonuç sayısı (1-40, varsayılan: 10)
- `language` (string, opsiyonel): Dil kodu (tr, en, fr, de vb., varsayılan: tr)

**Örnek Kullanım:**
```json
{
  "query": "Harry Potter",
  "max_results": 5,
  "language": "tr"
}
```

### 2. search_by_author
Belirli bir yazarın kitaplarını arama.

**Parametreler:**
- `author` (string): Yazar adı
- `max_results` (int, opsiyonel): Maksimum sonuç sayısı (varsayılan: 10)

**Örnek Kullanım:**
```json
{
  "author": "Orhan Pamuk",
  "max_results": 10
}
```

### 3. search_by_category
Kategoriye göre kitap arama.

**Parametreler:**
- `category` (string): Kitap kategorisi
- `max_results` (int, opsiyonel): Maksimum sonuç sayısı (varsayılan: 10)

**Örnek Kullanım:**
```json
{
  "category": "Fiction",
  "max_results": 15
}
```

### 4. get_book_info
Belirli bir kitabın detaylı bilgilerini alma.

**Parametreler:**
- `book_id` (string): Google Books API kitap ID'si

**Örnek Kullanım:**
```json
{
  "book_id": "zyTCAlFPjgYC"
}
```

## Yanıt Formatı

Tüm araçlar şu formatta yanıt döner:

```json
{
  "success": true,
  "totalItems": 1000,
  "query": "arama terimi",
  "books": [
    {
      "title": "Kitap Başlığı",
      "authors": ["Yazar Adı"],
      "publisher": "Yayınevi",
      "publishedDate": "2023",
      "description": "Kitap açıklaması...",
      "pageCount": 300,
      "categories": ["Kategori"],
      "averageRating": 4.5,
      "ratingsCount": 100,
      "language": "tr",
      "previewLink": "https://...",
      "infoLink": "https://...",
      "thumbnail": "https://..."
    }
  ]
}
```

## Kurulum ve Çalıştırma

### Yerel Geliştirme

1. Gereksinimleri yükleyin:
```bash
pip install -r requirements.txt
```

2. Serveri başlatın:
```bash
python server.py
```

### Smithery Deploy

Bu proje Smithery platformunda otomatik olarak deploy edilebilir. `smithery.yaml` dosyası gerekli konfigürasyonu içerir.

## Konfigürasyon

Smithery üzerinde aşağıdaki ayarları yapabilirsiniz:

- `default_language`: Varsayılan arama dili (varsayılan: "tr")
- `max_results_limit`: Maksimum sonuç limiti (varsayılan: 20, max: 40)

## API Limitleri

- Google Books API ücretsiz kullanım sınırları içinde çalışır
- Günlük 1000 sorgu limiti
- Sorgu başına maksimum 40 sonuç

## Lisans

MIT Lisansı ile lisanslanmıştır.

## Katkıda Bulunma

1. Projeyi fork edin
2. Yeni bir feature branch oluşturun
3. Değişikliklerinizi commit edin
4. Branch'inizi push edin
5. Pull request oluşturun

## İletişim

Sorularınız için issue açabilirsiniz. 
=======
# library-book-search-mcp
>>>>>>> 0d448af03999462217d1fe225dd31fd8853d5478
