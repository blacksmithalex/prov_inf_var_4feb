def f(a, b):
    if a > b or a == 9 or b == 9:
        return 0
    elif a == b:
        return 1
    else:
        return f(a + 1, b) + f(a * 2, b)

print(f(2, 12) * f(12, 42))