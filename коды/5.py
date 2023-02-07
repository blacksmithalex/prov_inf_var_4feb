def f(N):
    N = bin(N)[2:]
    s = sum([int(x) for x in N])
    if s % 2 == 0:
        return int('1' + N[2:] + '0', 2)
    else:
        return int('11' + N[2:] + '1', 2)

for n in range(1, 50):
    print(n, f(n))

