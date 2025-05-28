import asyncio
import logging
from mcp.server.fastmcp import FastMCP
from app import search_books, get_book_details, search_books_by_author, search_books_by_category

# Logging ayarla
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
    try:
        logger.info(f"Searching for books: query={query}, max_results={max_results}, language={language}")
        result = search_books(query, max_results, language)
        logger.info(f"Search completed: success={result.get('success', False)}")
        return result
    except Exception as e:
        logger.error(f"Error in search_library_books: {e}")
        return {"success": False, "error": str(e), "books": []}

@mcp.tool()
async def get_book_info(book_id: str) -> dict:
    """
    Belirli bir kitabın detaylı bilgilerini getirin.
    
    Args:
        book_id: Google Books API'den alınan kitap ID'si
    
    Returns:
        Kitabın detaylı bilgileri
    """
    try:
        logger.info(f"Getting book details for: {book_id}")
        result = get_book_details(book_id)
        logger.info(f"Book details completed: success={result.get('success', False)}")
        return result
    except Exception as e:
        logger.error(f"Error in get_book_info: {e}")
        return {"success": False, "error": str(e)}

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
    try:
        logger.info(f"Searching books by author: {author}")
        result = search_books_by_author(author, max_results)
        logger.info(f"Author search completed: success={result.get('success', False)}")
        return result
    except Exception as e:
        logger.error(f"Error in search_by_author: {e}")
        return {"success": False, "error": str(e), "books": []}

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
    try:
        logger.info(f"Searching books by category: {category}")
        result = search_books_by_category(category, max_results)
        logger.info(f"Category search completed: success={result.get('success', False)}")
        return result
    except Exception as e:
        logger.error(f"Error in search_by_category: {e}")
        return {"success": False, "error": str(e), "books": []}

async def main():
    """Ana fonksiyon"""
    try:
        logger.info("Starting Library Book Search MCP Server...")
        await mcp.run(transport="stdio")
    except Exception as e:
        logger.error(f"Server error: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())