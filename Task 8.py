
def calculate_payment(litres, fat, snf):
    """Validate one entry and calculate payment."""

    if litres <= 0:
        return None

    if not 2.0 <= fat <= 7.0:
        return None

    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = 30 + fat_steps * 0.40 + snf_steps * 0.30
    rate = round(rate, 2)

    return round(litres * rate, 2)


def main():
    """Read entries and calculate the total."""
    total = 0.0
    count = int(input("Number of entries: "))

    for i in range(count):
        print("\nEntry", i + 1)

        try:
            litres = float(input("Litres: "))
            fat = float(input("Fat: "))
            snf = float(input("SNF: "))
        except ValueError:
            print("Invalid numeric input; entry skipped.")
            continue

        payment = calculate_payment(litres, fat, snf)

        if payment is None:
            print("Invalid entry; entry skipped.")
        else:
            print(f"Payment: Rs. {payment:.2f}")
            total += payment

    print(f"\nTotal payment: Rs. {total:.2f}")


if __name__ == "__main__":
    main()
