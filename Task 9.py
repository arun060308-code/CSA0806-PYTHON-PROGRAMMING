
BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30


def rate_per_litre(fat, snf):
    """Calculate the rate per litre."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    return round(
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE, 2
    )


def payout(litres, fat, snf):
    """Calculate payment after validating the entry."""
    if litres <= 0:
        raise ValueError("Litres must be positive")

    if not 2.0 <= fat <= 7.0:
        raise ValueError("Fat must be between 2.0 and 7.0")

    if snf < 0:
        raise ValueError("SNF cannot be negative")

    return round(litres * rate_per_litre(fat, snf), 2)


def run_tests():
    """Test valid and invalid entries."""
    tests = [
        ((10, 3.5, 8.5), 300.00),
        ((8.5, 4.2, 8.7), 283.90),
        ((12, 3.1, 8.3), 333.60),
        ((1, 2.0, 8.5), 24.00),
        ((1, 7.0, 8.5), 44.00)
    ]

    for entry, expected in tests:
        actual = payout(*entry)
        assert actual == expected
        print(entry, "Expected:", expected, "Actual:", actual)

    invalid_entries = [
        (0, 3.5, 8.5),
        (10, 7.1, 8.5),
        (10, 3.5, -1)
    ]

    for entry in invalid_entries:
        try:
            payout(*entry)
            assert False, "Invalid entry was accepted"
        except ValueError:
            print(entry, "Rejected correctly")


if __name__ == "__main__":
    run_tests()
