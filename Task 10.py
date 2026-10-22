
from decimal import Decimal
from time import perf_counter


def benchmark(n):
    """Compare float and Decimal totals."""
    amounts = ["33.40"] * n

    start = perf_counter()
    float_total = 0.0

    for amount in amounts:
        float_total += float(amount)

    float_time = perf_counter() - start

    start = perf_counter()
    decimal_total = sum(
        (Decimal(amount) for amount in amounts),
        Decimal("0.00")
    )

    decimal_time = perf_counter() - start

    print("\nPayments:", n)
    print("Float total:", float_total)
    print("Decimal total:", decimal_total)
    print("Difference:", Decimal(str(float_total)) - decimal_total)
    print(f"Float time: {float_time:.6f} seconds")
    print(f"Decimal time: {decimal_time:.6f} seconds")


for count in [300, 6000, 150000]:
    benchmark(count)
