
"""Rate card and payment functions."""

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30


def rate_per_litre(fat, snf):
    """Return the rate per litre."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = BASE_RATE
    rate += fat_steps * FAT_STEP_VALUE
    rate += snf_steps * SNF_STEP_VALUE

    return round(rate, 2)


def payout(litres, fat, snf):
    """Return the payment amount."""
    rate = rate_per_litre(fat, snf)
    return round(litres * rate, 2)


if __name__ == "__main__":
    entries = [
        (10, 3.5, 8.5),
        (8.5, 4.2, 8.7),
        (12, 3.1, 8.3)
    ]

    for litres, fat, snf in entries:
        rate = rate_per_litre(fat, snf)
        pay = payout(litres, fat, snf)

        print(
            f"{litres:5} L  fat {fat} snf {snf}"
            f"  rate {rate:6.2f}  pay {pay:8.2f}"
        )
