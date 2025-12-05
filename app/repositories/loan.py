"""Repository for Loan database operations."""

from datetime import date
from decimal import Decimal
from typing import Sequence

from advanced_alchemy.repository import SQLAlchemySyncRepository
from litestar.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.models import Loan, LoanStatus


class LoanRepository(SQLAlchemySyncRepository[Loan]):
    """Repository for loan database operations."""

    model_type = Loan

    def get_active_loans(self) -> Sequence[Loan]:
        """Get loans with status == ACTIVE."""
        return self.list(Loan.status == LoanStatus.ACTIVE)

    def get_overdue_loans(self) -> Sequence[Loan]:
        """Get loans with due_date passed and status == ACTIVE."""
        today = date.today()
        return self.list(
            Loan.due_date < today,
            Loan.status == LoanStatus.ACTIVE,
        )

    def calculate_fine(self, loan_id: int) -> Decimal:
        """Calculate fine ($500 per day of delay)."""
        loan = self.get(loan_id)
        
        if loan.status != LoanStatus.ACTIVE:
            return Decimal("0.00")
        
        today = date.today()
        
        if today <= loan.due_date:
            return Decimal("0.00")
        
        days_overdue = (today - loan.due_date).days
        fine = Decimal(days_overdue) * Decimal("500.00")
        
        return fine

    def return_book(self, loan_id: int) -> Loan:
        """Process book return (update status to RETURNED, set return_dt, calculate and save fine_amount)."""
        loan = self.get(loan_id)
        
        if loan.status == LoanStatus.RETURNED:
            raise HTTPException(
                detail="Este préstamo ya fue devuelto",
                status_code=400,
            )
        
        loan.return_dt = date.today()
        
        fine = self.calculate_fine(loan_id)
        loan.fine_amount = fine
        
        loan.status = LoanStatus.RETURNED
        
        loan.book.stock += 1
        
        self.session.commit()
        self.session.refresh(loan)
        
        return loan

    def get_user_loan_history(self, user_id: int) -> Sequence[Loan]:
        """Get complete loan history for a user ordered by date."""
        return self.list(
            Loan.user_id == user_id,
            order_by=Loan.loan_dt.desc(),
        )


async def provide_loan_repo(db_session: Session) -> LoanRepository:
    """Provide loan repository instance with auto-commit."""
    return LoanRepository(session=db_session, auto_commit=True)