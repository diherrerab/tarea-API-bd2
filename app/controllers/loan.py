"""Controller for Loan endpoints."""

from typing import Sequence

from advanced_alchemy.exceptions import DuplicateKeyError, NotFoundError
from litestar import Controller, delete, get, patch, post
from litestar.di import Provide
from litestar.dto import DTOData

from app.controllers import duplicate_error_handler, not_found_error_handler
from app.dtos.loan import LoanCreateDTO, LoanReadDTO, LoanUpdateDTO
from app.models import Loan
from app.repositories.loan import LoanRepository, provide_loan_repo


class LoanController(Controller):
    """Controller for loan management operations."""

    path = "/loans"
    tags = ["loans"]
    return_dto = LoanReadDTO
    dependencies = {"loans_repo": Provide(provide_loan_repo)}
    exception_handlers = {
        NotFoundError: not_found_error_handler,
        DuplicateKeyError: duplicate_error_handler,
    }

    @get("/")
    async def list_loans(self, loans_repo: LoanRepository) -> Sequence[Loan]:
        """Get all loans."""
        return loans_repo.list()

    @get("/{id:int}")
    async def get_loan(self, id: int, loans_repo: LoanRepository) -> Loan:
        """Get a loan by ID."""
        return loans_repo.get(id)

    @post("/", dto=LoanCreateDTO)
    async def create_loan(
        self,
        data: DTOData[Loan],
        loans_repo: LoanRepository,
    ) -> Loan:
        """Create a new loan."""

        return loans_repo.add(data.create_instance())

    @patch("/{id:int}", dto=LoanUpdateDTO)
    async def update_loan(
        self,
        id: int,
        data: DTOData[Loan],
        loans_repo: LoanRepository,
    ) -> Loan:
        """Update a loan by ID."""
        loan, _ = loans_repo.get_and_update(match_fields="id", id=id, **data.as_builtins())

        return loan

    @delete("/{id:int}")
    async def delete_loan(self, id: int, loans_repo: LoanRepository) -> None:
        """Delete a loan by ID."""
        loans_repo.delete(id)
    
    @get("/active")
    async def get_active_loans(self, loans_repo: LoanRepository) -> Sequence[Loan]:
        """Get active loans."""
        return loans_repo.get_active_loans()

    @get("/overdue")
    async def get_overdue_loans(self, loans_repo: LoanRepository) -> Sequence[Loan]:
        """Get overdue loans."""
        return loans_repo.get_overdue_loans()

    @post("/{loan_id:int}/return")
    async def return_loan(
        self,
        loan_id: int,
        loans_repo: LoanRepository,
    ) -> Loan:
        """Return a book."""
        return loans_repo.return_book(loan_id)

    @get("/user/{user_id:int}")
    async def get_user_loans(
        self,
        user_id: int,
        loans_repo: LoanRepository,
    ) -> Sequence[Loan]:
        """Get user loan history."""
        return loans_repo.get_user_loan_history(user_id)
