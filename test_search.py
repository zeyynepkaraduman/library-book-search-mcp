#!/usr/bin/env python3
"""
Kitap arama fonksiyonlarını test et
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import search_books, search_books_by_author, search_books_by_category

def test_search_functions():
    """Kitap arama işlevlerini test et"""
    
    print("=== KİTAP ARAMA TESTLERİ ===\n")
    
    # 1. Genel kitap arama
    print("1. Genel Kitap Arama: 'Python programming'")
    result = search_books("Python programming", max_results=2, language="en")
    if result["success"]:
        print(f"✅ {result['totalItems']} sonuç bulundu")
        for i, book in enumerate(result["books"], 1):
            print(f"   {i}. {book['title']} - {', '.join(book['authors'])}")
    else:
        print(f"❌ Hata: {result['error']}")
    print()
    
    print("=== TEST TAMAMLANDI ===")

if __name__ == "__main__":
    test_search_functions() 