
from decimal import Decimal, ROUND_HALF_UP

# Original rate card
BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")

# Seasonal rate card
SEASON_BASE_RATE = Decimal("32.00")
SEASON_FAT_STEP_VALUE = Decimal("0.45")

# Bonus rules
BONUS_LIMIT = Decimal("500")
BONUS_PER_LITRE = Decimal("0.50")


def round_money(value):
    """Round a monetary amount to two decimal places."""
    return value.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )


def count_steps(value, standard):
    """Count 0.1 percentage steps, rounding half up."""
    difference = (Decimal(str(value)) - Decimal(str(standard)))
    steps = difference / Decimal("0.1")

    return int(steps.quantize(
        Decimal("1"),
        rounding=ROUND_HALF_UP
    ))


def rate_per_litre(fat, snf, seasonal=False):
    """Calculate the rate using the selected rate card."""
    if seasonal:
        base = SEASON_BASE_RATE
        fat_value = SEASON_FAT_STEP_VALUE
    else:
        base = BASE_RATE
        fat_value = FAT_STEP_VALUE

    fat_steps = count_steps(fat, "3.5")
    snf_steps = count_steps(snf, "8.5")

    rate = (
        base
        + fat_steps * fat_value
        + snf_steps * SNF_STEP_VALUE
    )

    return round_money(rate)


def payout(litres, fat, snf, seasonal=False):
    """Calculate the payment before any ten-day bonus."""
    litres = Decimal(str(litres))

    if litres <= 0:
        raise ValueError("Litres must be positive")

    if not 2.0 <= float(fat) <= 7.0:
        raise ValueError("Fat must be between 2.0 and 7.0")

    if float(snf) < 0:
        raise ValueError("SNF cannot be negative")

    rate = rate_per_litre(fat, snf, seasonal)
    return round_money(litres * rate)


def ten_day_payment(entries, seasonal=False):
    """Calculate payments and apply the ten-day bonus."""
    total_litres = sum(
        (Decimal(str(entry[0])) for entry in entries),
        Decimal("0")
    )

    total_payment = sum(
        (
            payout(litres, fat, snf, seasonal)
            for litres, fat, snf in entries
        ),
        Decimal("0.00")
    )

    bonus = Decimal("0.00")

    if total_litres > BONUS_LIMIT:
        bonus = round_money(total_litres * BONUS_PER_LITRE)

    return round_money(total_payment + bonus), bonus


# Example ten-day records: (litres, fat, SNF)
entries = [
    (250, "3.56", "8.57"),
    (260, "4.20", "8.70")
]

for seasonal in [False, True]:
    total, bonus = ten_day_payment(entries, seasonal)

    print("Seasonal rates:", seasonal)
    print("Ten-day litres:", sum(
        (Decimal(str(e[0])) for e in entries),
        Decimal("0")
    ))
    print("Bonus:", bonus)
    print("Total payment:", total)
    print()
