
expected = [100, 200, 300]
actual = [100, 250, 300]

for i, value in enumerate(actual):
    if value != expected[i]:
        print(
            f"Mismatch at position {i}: "
            f"expected={expected[i]}, actual={value}"
        )


for i, (exp, act) in enumerate(zip(expected, actual)):
    if exp != act:
        print(i, exp, act)
