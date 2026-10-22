
BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

fat = 4.2
snf = 8.7
litres = 8.5

fat_steps = round((fat - STANDARD_FAT) / 0.1)
snf_steps = round((snf - STANDARD_SNF) / 0.1)

rate = BASE_RATE + fat_steps * FAT_STEP_VALUE
rate += snf_steps * SNF_STEP_VALUE
rate = round(rate, 2)

amount = round(litres * rate, 2)

print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print(f"Rate per litre: Rs. {rate:.2f}")
print(f"Payment: Rs. {amount:.2f}")

# Compare rounding methods
for fat_value in [4.2, 3.1]:
    difference = (fat_value - STANDARD_FAT) / 0.1
    print("\nFat:", fat_value)
    print("round:", round(difference))
    print("int:", int(difference))
    print("floor:", __import__("math").floor(difference))
