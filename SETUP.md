# Kurulum Rehberi

## Smithery'de Deploy Etme

### 1. Repository URL
```
https://github.com/zeyynepkaraduman/library-book-search-mcp
```

### 2. Smithery Konfigürasyonu

Smithery platformunda MCP oluştururken şu ayarları kullanın:

```yaml
default_language: "tr"
max_results_limit: 20
```

### 3. Kullanılabilir Diller

- `tr` - Türkçe
- `en` - İngilizce  
- `fr` - Fransızca
- `de` - Almanca
- `es` - İspanyolca
- `it` - İtalyanca

### 4. Test Sorguları

Kurulum sonrası test için örnek sorgular:

```json
{
  "tool": "search_library_books",
  "query": "Harry Potter",
  "max_results": 5,
  "language": "tr"
}
```

```json
{
  "tool": "search_by_author", 
  "author": "Orhan Pamuk",
  "max_results": 10
}
```

```json
{
  "tool": "search_by_category",
  "category": "Fiction", 
  "max_results": 15
}
```

### 5. Troubleshooting

- API limiti aşılırsa 24 saat bekleyin
- Türkçe karakterlerde sorun varsa `language: "en"` deneyin
- Boş sonuç gelirse sorguyu değiştirin

### 6. İletişim

Sorularınız için GitHub Issues açabilirsiniz. 