def f(x, y, p):
    if x + y >= 52 and p == 4:
        return True
    elif x + y < 52 and p == 4:
        return False
    elif x + y >= 52:
        return False
    else:
        if p % 2 == 1:
            return f(x + 2, y, p + 1) or f(x, y + 2, p + 1) or f(x * 3, y, p + 1) or f(x, y * 3, p + 1)
        else:
            return f(x + 2, y, p + 1) and f(x, y + 2, p + 1) and f(x * 3, y, p + 1) and f(x, y * 3, p + 1)

for S in range(1, 46 + 1):
    if f(5, S, 1):
        print(S)
