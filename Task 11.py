
from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")


def money(value):
    """Round a decimal amount to two decimal places."""
    return value.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )


def rate_per_litre(fat, snf):
    """Calculate the rate using decimal arithmetic."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = (
        BASE_RATE
        + Decimal(fat_steps) * FAT_STEP_VALUE
        + Decimal(snf_steps) * SNF_STEP_VALUE
    )

    return money(rate)


def payout(litres, fat, snf):
    """Return the payment rounded to paise."""
    litres = Decimal(str(litres))
    rate = rate_per_litre(fat, snf)

    return money(litres * rate)


payment = payout("8.5", 4.2, 8.7)
print("Payment:", payment)
