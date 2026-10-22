
BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30


def rate_per_litre(fat, snf):
    """Calculate the milk price per litre."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = BASE_RATE
    rate += fat_steps * FAT_STEP_VALUE
    rate += snf_steps * SNF_STEP_VALUE

    return round(rate, 2)


def payout(litres, fat, snf):
    """Calculate the payment for a milk delivery."""
    rate = rate_per_litre(fat, snf)
    return round(litres * rate, 2)


def ten_day_total(payments):
    """Calculate the total of multiple payments."""
    total = 0.0

    for payment in payments:
        total += payment

    return round(total, 2)


amount1 = payout(10, 3.5, 8.5)
amount2 = payout(8.5, 4.2, 8.7)
amount3 = payout(12, 3.1, 8.3)

print("Payment 1:", amount1)
print("Payment 2:", amount2)
print("Payment 3:", amount3)
print("Ten-day total:",
      ten_day_total([amount1, amount2, amount3]))
