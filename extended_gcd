def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

# 예제
a, b = 30, 20
gcd, x, y = extended_gcd(a, b)
print(f"gcd({a}, {b}) = {gcd}")
print(f"Coefficients: x = {x}, y = {y}")
