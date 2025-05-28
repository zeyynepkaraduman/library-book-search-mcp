from mcp.server.fastmcp import FastMCP
from app import search_books, get_book_details, search_books_by_author, search_books_by_category

# Initialize MCP server
mcp = FastMCP("library-book-search-mcp")

@mcp.tool()
async def search_library_books(query: str, max_results: int = 10, language: str = "tr") -> dict:
    """
    Kütüphanede kitap arama - Google Books API kullanarak kitap, yazar veya konu arayın.
    
    Args:
        query: Aranacak kitap adı, yazar adı veya konu
        max_results: Döndürülecek maksimum sonuç sayısı (1-40 arası, varsayılan: 10)
        language: Aranacak dil kodu (tr, en, fr, de vb. - varsayılan: tr)
    
    Returns:
        Bulunan kitapların listesi ve detayları
    """
    result = search_books(query, max_results, language)
    return result

@mcp.tool()
async def get_book_info(book_id: str) -> dict:
    """
    Belirli bir kitabın detaylı bilgilerini getirin.
    
    Args:
        book_id: Google Books API'den alınan kitap ID'si
    
    Returns:
        Kitabın detaylı bilgileri
    """
    result = get_book_details(book_id)
    return result

@mcp.tool()
async def search_by_author(author: str, max_results: int = 10) -> dict:
    """
    Belirli bir yazarın kitaplarını arayın.
    
    Args:
        author: Yazar adı
        max_results: Döndürülecek maksimum sonuç sayısı (varsayılan: 10)
    
    Returns:
        Yazarın kitaplarının listesi
    """
    result = search_books_by_author(author, max_results)
    return result

@mcp.tool()
async def search_by_category(category: str, max_results: int = 10) -> dict:
    """
    Belirli bir kategorideki kitapları arayın.
    
    Args:
        category: Kitap kategorisi (örn: "Fiction", "Science", "History", "Romance")
        max_results: Döndürülecek maksimum sonuç sayısı (varsayılan: 10)
    
    Returns:
        Kategorideki kitapların listesi
    """
    result = search_books_by_category(category, max_results)
    return result

if __name__ == "__main__":
    mcp.run(transport="stdio")