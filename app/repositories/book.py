"""Repository for Book database operations."""

from typing import Sequence

from advanced_alchemy.repository import SQLAlchemySyncRepository
from litestar.exceptions import HTTPException
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models import Book, Review, book_categories


class BookRepository(SQLAlchemySyncRepository[Book]):
    """Repository for book database operations."""

    model_type = Book

    def get_available_books(self) -> Sequence[Book]:
        """Get books with stock > 0."""
        return self.list(Book.stock > 0)

    def find_by_category(self, category_id: int) -> Sequence[Book]:
        """Find books by category."""
        statement = (
            select(Book)
            .join(book_categories)
            .where(book_categories.c.category_id == category_id)
        )
        return self.session.execute(statement).scalars().all()

    def get_most_reviewed_books(self, limit: int = 10) -> Sequence[Book]:
        """Get books ordered by review count."""
        statement = (
            select(Book)
            .outerjoin(Review)
            .group_by(Book.id)
            .order_by(func.count(Review.id).desc())
            .limit(limit)
        )
        return self.session.execute(statement).scalars().all()

    def update_stock(self, book_id: int, quantity: int) -> Book:
        """Update book stock, validate it doesn't go negative."""
        book = self.get(book_id)
        
        new_stock = book.stock + quantity
        
        if new_stock < 0:
            raise HTTPException(
                detail="El stock no puede ser negativo",
                status_code=400,
            )
        
        book.stock = new_stock
        self.session.commit()
        self.session.refresh(book)
        
        return book

    def search_by_author(self, author_name: str) -> Sequence[Book]:
        """Search books by author name (partial match using ilike)."""
        return self.list(Book.author.ilike(f"%{author_name}%"))


async def provide_book_repo(db_session: Session) -> BookRepository:
    """Provide book repository instance with auto-commit."""
    return BookRepository(session=db_session, auto_commit=True)