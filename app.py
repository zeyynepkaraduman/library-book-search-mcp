import requests
import json
from typing import Dict

def search_books(query: str, max_results: int = 10, language: str = "tr") -> Dict:
    try:
        base_url = "https://www.googleapis.com/books/v1/volumes"
        params = {
            "q": query,
            "maxResults": min(max_results, 40),
            "langRestrict": language,
            "printType": "books"
        }
        
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        books = []
        for item in data.get("items", []):
            volume_info = item.get("volumeInfo", {})
            book = {
                "title": volume_info.get("title", "Bilinmeyen Başlık"),
                "authors": volume_info.get("authors", ["Bilinmeyen Yazar"]),
                "publisher": volume_info.get("publisher", "Bilinmeyen Yayınevi"),
                "publishedDate": volume_info.get("publishedDate", "Tarih belirtilmemiş"),
                "description": volume_info.get("description", "Açıklama mevcut değil")[:500] + "..." if volume_info.get("description", "") else "Açıklama mevcut değil",
                "pageCount": volume_info.get("pageCount", 0),
                "categories": volume_info.get("categories", []),
                "averageRating": volume_info.get("averageRating"),
                "ratingsCount": volume_info.get("ratingsCount"),
                "language": volume_info.get("language", ""),
                "previewLink": volume_info.get("previewLink", ""),
                "infoLink": volume_info.get("infoLink", ""),
                "thumbnail": volume_info.get("imageLinks", {}).get("thumbnail", "")
            }
            books.append(book)
        
        return {
            "success": True,
            "totalItems": data.get("totalItems", 0),
            "query": query,
            "books": books
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": f"Hata: {str(e)}",
            "books": []
        }

def get_book_details(book_id: str) -> Dict:
    try:
        url = f"https://www.googleapis.com/books/v1/volumes/{book_id}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        volume_info = data.get("volumeInfo", {})
        
        return {
            "success": True,
            "book": {
                "id": data.get("id", ""),
                "title": volume_info.get("title", ""),
                "subtitle": volume_info.get("subtitle", ""),
                "authors": volume_info.get("authors", []),
                "publisher": volume_info.get("publisher", ""),
                "publishedDate": volume_info.get("publishedDate", ""),
                "description": volume_info.get("description", ""),
                "pageCount": volume_info.get("pageCount", 0),
                "categories": volume_info.get("categories", []),
                "averageRating": volume_info.get("averageRating"),
                "ratingsCount": volume_info.get("ratingsCount"),
                "language": volume_info.get("language", ""),
                "previewLink": volume_info.get("previewLink", ""),
                "infoLink": volume_info.get("infoLink", ""),
                "thumbnail": volume_info.get("imageLinks", {}).get("thumbnail", ""),
                "smallThumbnail": volume_info.get("imageLinks", {}).get("smallThumbnail", "")
            }
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": f"Hata: {str(e)}"
        }

def search_books_by_author(author: str, max_results: int = 10) -> Dict:
    query = f"inauthor:{author}"
    return search_books(query, max_results)

def search_books_by_category(category: str, max_results: int = 10) -> Dict:
    query = f"subject:{category}"
    return search_books(query, max_results)
