import pytest

from kifbazar.core.money import Money


@pytest.mark.parametrize(
    ("amount", "currency"),
    [
        (100, "IRR"),
        (0, "IRR"),
        (-100, "IRR"),
        (1_000_000, "USD"),
    ],
)
def test_money_creation(amount: int, currency: str) -> None:
    money = Money(amount, currency)

    assert money.amount == amount
    assert money.currency == currency


def test_currency_is_normalized() -> None:
    money = Money(100, " irr ")

    assert money.currency == "IRR"


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (100, 200, 300),
        (0, 200, 200),
        (-100, 200, 100),
        (-100, -200, -300),
    ],
)
def test_money_addition(
    left: int,
    right: int,
    expected: int,
) -> None:
    result = Money(left, "IRR") + Money(right, "IRR")

    assert result == Money(expected, "IRR")


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (500, 200, 300),
        (100, 100, 0),
        (100, 200, -100),
    ],
)
def test_money_subtraction(
    left: int,
    right: int,
    expected: int,
) -> None:
    result = Money(left, "IRR") - Money(right, "IRR")

    assert result == Money(expected, "IRR")


@pytest.mark.parametrize(
    ("amount", "multiplier", "expected"),
    [
        (100, 2, 200),
        (100, 0, 0),
        (100, -2, -200),
    ],
)
def test_money_multiplication(
    amount: int,
    multiplier: int,
    expected: int,
) -> None:
    result = Money(amount, "IRR") * multiplier

    assert result == Money(expected, "IRR")


def test_reverse_multiplication() -> None:
    result = 3 * Money(100, "IRR")

    assert result == Money(300, "IRR")


def test_money_comparison() -> None:
    assert Money(200, "IRR") > Money(100, "IRR")
    assert Money(100, "IRR") < Money(200, "IRR")


def test_different_currencies_cannot_be_added() -> None:
    with pytest.raises(ValueError, match="Currency mismatch"):
        Money(100, "IRR") + Money(10, "USD")


def test_different_currencies_cannot_be_subtracted() -> None:
    with pytest.raises(ValueError, match="Currency mismatch"):
        Money(100, "IRR") - Money(10, "USD")


def test_different_currencies_cannot_be_compared() -> None:
    with pytest.raises(ValueError, match="Currency mismatch"):
        assert Money(100, "IRR") < Money(10, "USD")


@pytest.mark.parametrize(
    "invalid_amount",
    [
        100.5,
        0.1 + 0.2,
        True,
        "100",
        None,
    ],
)
def test_invalid_amount_is_rejected(invalid_amount: object) -> None:
    with pytest.raises(TypeError, match="integer"):
        Money(invalid_amount, "IRR")  # type: ignore[arg-type]


def test_float_precision_problem() -> None:
    # Binary floating-point cannot represent 0.1 and 0.2 exactly.
    assert 0.1 + 0.2 != 0.3

    # Therefore, float must never be accepted as a monetary amount.
    with pytest.raises(TypeError):
        Money(0.1 + 0.2, "USD")  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "invalid_currency",
    [
        "",
        "IR",
        "IRRR",
        "12A",
        "123",
    ],
)
def test_invalid_currency_is_rejected(invalid_currency: str) -> None:
    with pytest.raises(ValueError):
        Money(100, invalid_currency)


def test_money_is_immutable() -> None:
    money = Money(100, "IRR")

    with pytest.raises(AttributeError):
        money.amount = 200  # type: ignore[misc]


def test_money_currency_is_immutable() -> None:
    money = Money(100, "IRR")

    with pytest.raises(AttributeError):
        money.currency = "USD"  # type: ignore[misc]
