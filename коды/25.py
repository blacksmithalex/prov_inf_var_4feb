for a1 in range(10):
    a = int('2' + str(a1) + '167')
    if a % 159 == 0:
        print(a, a // 159)

for a1 in range(10):
    for a2 in range(10):
        a = int('2' + str(a1) + '1' + str(a2) + '67')
        if a % 159 == 0:
            print(a, a // 159)

for a1 in range(10):
    for a2 in range(10):
        for a3 in range(10):
            a = int('2' + str(a1) + '1' + str(a2) + str(a3) + '67')
            if a % 159 == 0:
                print(a, a // 159)
