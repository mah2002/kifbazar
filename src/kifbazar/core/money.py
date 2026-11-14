from __future__ import annotations

import re
from dataclasses import dataclass
from functools import total_ordering
from types import NotImplementedType


@total_ordering
@dataclass(frozen=True, slots=True)
class Money:
    """
    Immutable monetary value stored as an integer in the smallest unit.

    Negative amounts are allowed because financial ledgers need to represent
    debits, reversals, and adjustments. Wallet services are responsible for
    preventing invalid negative balances.

    Float values are rejected because binary floating-point arithmetic
    cannot reliably represent decimal monetary values.
    """

    amount: int
    currency: str

    def __post_init__(self) -> None:
        if isinstance(self.amount, bool) or not isinstance(self.amount, int):
            raise TypeError("Money amount must be an integer.")

        if not isinstance(self.currency, str):
            raise TypeError("Currency must be a string.")

        normalized_currency = self.currency.strip().upper()

        if not re.fullmatch(r"[A-Z]{3}", normalized_currency):
            raise ValueError("Currency must be a three-letter code.")

        object.__setattr__(self, "currency", normalized_currency)

    def _ensure_same_currency(self, other: Money) -> None:
        if self.currency != other.currency:
            raise ValueError(f"Currency mismatch: {self.currency} != {other.currency}")

    def __add__(self, other: object) -> Money | NotImplementedType:
        if not isinstance(other, Money):
            return NotImplemented

        self._ensure_same_currency(other)

        return Money(
            amount=self.amount + other.amount,
            currency=self.currency,
        )

    def __sub__(self, other: object) -> Money | NotImplementedType:
        if not isinstance(other, Money):
            return NotImplemented

        self._ensure_same_currency(other)

        return Money(
            amount=self.amount - other.amount,
            currency=self.currency,
        )

    def __neg__(self) -> Money:
        return Money(
            amount=-self.amount,
            currency=self.currency,
        )

    def __mul__(self, multiplier: object) -> Money | NotImplementedType:
        if isinstance(multiplier, bool) or not isinstance(multiplier, int):
            return NotImplemented

        return Money(
            amount=self.amount * multiplier,
            currency=self.currency,
        )

    def __rmul__(self, multiplier: object) -> Money | NotImplementedType:
        return self.__mul__(multiplier)

    def __lt__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Money):
            return NotImplemented

        self._ensure_same_currency(other)

        return self.amount < other.amount

    def __str__(self) -> str:
        return f"{self.amount} {self.currency}"
