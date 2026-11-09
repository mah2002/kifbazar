# KifBazar

**A Wallet-Backed Marketplace API**

KifBazar is a backend project built with Python and FastAPI, exploring reliable financial transactions and core marketplace operations.

The project focuses on backend engineering challenges such as wallet management, double-entry accounting, transaction safety, concurrency control, and idempotent API operations.

**Tech Stack:** Python · FastAPI · PostgreSQL · SQLAlchemy · Redis · Docker

**Status:** V1 in development.

> All financial transactions are simulated using a mock payment provider. No real payments are processed.

## Key Features & Engineering Focus

- **Wallet & Double-Entry Ledger:** Accurate financial tracking with immutable transaction records.
- **Atomic Checkout:** Maintaining consistency across wallet balances, inventory, orders, and ledger entries.
- **Concurrency Control:** Preventing overselling and concurrent wallet overdrafts.
- **Idempotent Operations:** Handling duplicate requests and payment callbacks safely.
- **Payment Abstraction:** A pluggable payment provider architecture.
- **Advanced Search:** Planned PostgreSQL full-text and fuzzy search capabilities.

*Features are under development and should not be considered implemented unless explicitly demonstrated in the source code and tests.*

## Architecture

The project follows a layered architecture with clear separation between:

- API endpoints and request validation
- Domain entities and business rules
- Application services and use cases
- Data access and repositories
- External service providers

Architecture decisions are documented using ADRs.

## Technical Stack

Python 3.12+ · FastAPI · Pydantic v2 · SQLAlchemy 2 · PostgreSQL · Alembic · Redis · Docker · pytest · GitHub Actions

## Scope

KifBazar is a portfolio-oriented backend engineering project. It uses simulated payments and does not process real financial transactions.

## License

MIT
