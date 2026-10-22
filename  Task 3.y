# Task 3: Variables and Constants

# Named constants
BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

# Display the constants
print("Base Rate:", BASE_RATE)
print("Standard Fat:", STANDARD_FAT)
print("Standard SNF:", STANDARD_SNF)
print("Fat Step Value:", FAT_STEP_VALUE)
print("SNF Step Value:", SNF_STEP_VALUE)

# Dynamic typing
value = 10
print("Value:", value, "Type:", type(value))

value = "Milk"
print("Value:", value, "Type:", type(value))

# Multiple assignment and swapping
a = 10
b = 20

print("Before swapping:", a, b)

a, b = b, a

print("After swapping:", a, b)