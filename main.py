def pyramid_number(n: int) -> int:
    return int((n * (n + 1) * (2 * n + 1)) / 6)

print(pyramid_number(1))  # 1
print(pyramid_number(2))  # 4
print(pyramid_number(3))  # 10
print(pyramid_number(4))  # 20
