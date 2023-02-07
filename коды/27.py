file = open('27_B.txt')
N = int(file.readline())
dmin = 10000
s = 0
for _ in range(N):
    a, b, c = sorted([int(x) for x in file.readline().split()])
    s += c
    if (c - b) % 91 != 0 and (c - b) < dmin:
        dmin = c - b
    elif (c - a) % 91 != 0 and (c - a) < dmin:
        dmin = c - a
if s % 91 != 0:
    print(s)
else:
    print(s - dmin)
