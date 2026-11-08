kifbazar
> Prepaid-wallet marketplace API: double-entry ledger, idempotent checkout, atomic inventory.
> FastAPI · PostgreSQL · Redis · Docker
Status: V1 in development. Checkboxes below show what is actually done.
All money is simulated through a mock payment provider. No real payments are processed.
What it is
Customers top up a wallet, browse a categorized catalog, and pay for orders from the wallet balance.
The project focuses on the hard parts of this domain rather than on UI:
Money correctness: every balance change is an immutable double-entry ledger record.
Concurrency safety: simultaneous checkouts can never oversell stock or overdraw a wallet.
Idempotency: retried requests and duplicated payment callbacks never charge or credit twice.
Query performance: indexed search and category queries, backed by `EXPLAIN ANALYZE` evidence (V2).
Roadmap
V1: Core (money + checkout)
[ ] Registration and login (JWT, hashed passwords)
[ ] Wallet with immutable double-entry ledger
[ ] Wallet top-up through a pluggable `PaymentProvider` (mock implementation, callback + verify)
[ ] Catalog: products and single-level categories
[ ] Atomic checkout: stock decrement, wallet debit, order, and ledger entries in one transaction
[ ] `Idempotency-Key` support on top-up and checkout
[ ] Tests against a real PostgreSQL, including concurrency tests
[ ] Docker Compose setup and CI (lint, type-check, tests)
V2: Depth
[ ] Full-text search (`tsvector` + GIN) and fuzzy matching (`pg_trgm`), combined filters, keyset pagination
[ ] Hierarchical categories (recursive CTE, single-query subtree lookups)
[ ] Public and private product images (S3-compatible storage, presigned URLs for private files)
[ ] Temporary stock holds with TTL (Redis) and rate limiting
[ ] Measured query benchmarks in `docs/benchmarks.md`
V3: Operations and events
[ ] Transactional outbox and event publishing
[ ] Metrics, dashboards, health and readiness endpoints
[ ] Sales reporting data flow
Design rules
Rule	How it is enforced
No floating-point money	Amounts stored as integer minor units
Ledger is append-only	No update or delete paths; corrections are reversal entries
No negative balance or stock	Database constraints plus row locking
No double charge	Idempotency keys, stored with the original response
Duplicate callbacks are harmless	Payment intents are state machines; verification is idempotent
Private files stay private	Authorization check before every presigned URL, covered by tests
Architecture decisions are recorded in `docs/adr/`.
Tech stack
Python 3.12+, FastAPI, Pydantic v2, SQLAlchemy 2 (async), Alembic, PostgreSQL,
Redis (V2), MinIO (V2), pytest, Docker and Docker Compose, GitHub Actions,
`uv` (packages), `ruff` (lint/format), `mypy` (types).
Planned project layout
```
src/kifbazar/
  api/          # routers, request/response schemas, dependencies
  domain/       # entities and business rules (no framework imports)
  services/     # use cases: checkout, top-up, catalog
  repositories/ # database access
  providers/    # PaymentProvider interface and implementations
  core/         # settings, security, logging
alembic/        # migrations
tests/          # unit, integration (real PostgreSQL), concurrency
docs/           # ADRs, diagrams, benchmarks
```
Running locally
These commands become valid as V1 lands:
```bash
cp .env.example .env
docker compose up -d
uv run alembic upgrade head
uv run pytest
```
API docs will be served at `/docs` (OpenAPI).
Honest scope
Out of scope on purpose: real money movement, a production payment gateway, a full frontend,
discounts and coupons, multi-language support. The payment layer is abstracted so a real
gateway adapter can be added without changing checkout logic.
License
MIT
