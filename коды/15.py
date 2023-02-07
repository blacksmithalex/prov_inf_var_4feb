def f(x, y, A):
    l1 = x > A
    l2 = y > A
    l3 = y - 2 * x + 12 != 0
    return l1 or l2 or l3

for A in range(100):
    flag = True
    for x in range(300):
        for y in range(300):
            if f(x, y, A) == False:
                flag = False
    if flag:
        print(A)