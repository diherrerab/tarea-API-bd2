"""Database models for the library management system."""

import enum
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import Column, Enum, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship


# tabla relacion many to many entre Book y Category
book_categories = Table(
    "book_categories",
    BigIntAuditBase.metadata,
    Column("book_id", ForeignKey("books.id"), primary_key=True),
    Column("category_id", ForeignKey("categories.id"), primary_key=True),
)


class LoanStatus(str, enum.Enum):
    """Loan status enumeration."""
    
    ACTIVE = "ACTIVE"
    RETURNED = "RETURNED"
    OVERDUE = "OVERDUE"


class User(BigIntAuditBase):
    """User model with audit fields."""

    __tablename__ = "users"

    username: Mapped[str] = mapped_column(unique=True)
    fullname: Mapped[str]
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    phone: Mapped[str | None]
    address: Mapped[str | None]
    is_active: Mapped[bool] = mapped_column(default=True)

    loans: Mapped[list["Loan"]] = relationship(back_populates="user")
    reviews: Mapped[list["Review"]] = relationship(back_populates="user")


class Book(BigIntAuditBase):
    """Book model with audit fields."""

    __tablename__ = "books"

    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str]
    isbn: Mapped[str] = mapped_column(unique=True)
    pages: Mapped[int]
    published_year: Mapped[int]
    stock: Mapped[int] = mapped_column(default=1)
    description: Mapped[str | None]
    language: Mapped[str]
    publisher: Mapped[str | None]

    loans: Mapped[list["Loan"]] = relationship(back_populates="book")
    categories: Mapped[list["Category"]] = relationship(
        secondary=book_categories,
        back_populates="books"
    )
    reviews: Mapped[list["Review"]] = relationship(back_populates="book")


class Category(BigIntAuditBase):
    """Category model with audit fields."""

    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str | None]

    books: Mapped[list["Book"]] = relationship(
        secondary=book_categories,
        back_populates="categories"
    )


class Review(BigIntAuditBase):
    """Review model with audit fields."""

    __tablename__ = "reviews"

    rating: Mapped[int]
    comment: Mapped[str]
    review_date: Mapped[date]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))

    user: Mapped["User"] = relationship(back_populates="reviews")
    book: Mapped["Book"] = relationship(back_populates="reviews")


class Loan(BigIntAuditBase):
    """Loan model with audit fields."""

    __tablename__ = "loans"

    loan_dt: Mapped[date] = mapped_column(default=datetime.today)
    return_dt: Mapped[date | None]
    due_date: Mapped[date]
    fine_amount: Mapped[Decimal | None] = mapped_column(nullable=True)
    status: Mapped[LoanStatus] = mapped_column(
        Enum(LoanStatus, native_enum=False),
        default=LoanStatus.ACTIVE
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))

    user: Mapped[User] = relationship(back_populates="loans")
    book: Mapped[Book] = relationship(back_populates="loans")


@dataclass
class PasswordUpdate:
    """Password update request."""

    current_password: str
    new_password: str


@dataclass
class BookStats:
    """Book statistics data."""

    total_books: int
    average_pages: float
    oldest_publication_year: int | None
    newest_publication_year: int | None