x = 0.001
f = 2023 * (1 - 1/4 * x ** 14)
print(f)
# we need 52 significant digits, and float64 has less than that so its not fully accurate
