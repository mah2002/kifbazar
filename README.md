# KifBazar

**A Wallet-Backed Marketplace API**

KifBazar is a backend project built with Python and FastAPI, exploring reliable financial transactions and core marketplace operations.

The project focuses on backend engineering challenges such as wallet management, double-entry accounting, transaction safety, concurrency control, and idempotent API operations.

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

## Tech Stack

Python 3.12+ · FastAPI · Pydantic v2 · SQLAlchemy 2 · PostgreSQL · Alembic · Redis · Docker · uv · pytest · Ruff · Mypy · GitHub Actions

## Getting Started

### Prerequisites

- Python 3.12+
- Git
- uv

### Installation

Clone the repository:

```bash
git clone [<REPOSITORY_URL>](https://github.com/mah2002/kifbazar)
cd kifbazar
```

Install project dependencies and create the virtual environment:

```bash
uv sync
```

### Configuration

If an `.env.example` file exists, create your local environment file:

```powershell
Copy-Item .env.example .env
```

Configure the required environment variables before running the application.

### Run Tests

```bash
uv run pytest
```

### Code Quality

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src
```

### Run the Application

Once the application entry point and required services are configured:

```bash
uv run uvicorn kifbazar.main:app --reload
```

API documentation:

http://127.0.0.1:8000/docs

*The startup command assumes `src/kifbazar/main.py` exposes a FastAPI instance named `app`. Required infrastructure services must be running.*

## License

MIT
