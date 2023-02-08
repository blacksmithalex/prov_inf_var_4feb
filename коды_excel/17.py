file = open('17.txt')
a = [int(x) for x in file]
file.close()
m9 = -100000
for x in a:
    if str(x)[-1] == '9' and x > m9:
        m9 = x

count, sm = 0, 10**11
for i in range(len(a) - 1):
    l1 = str(a[i])[-1] == '9' and str(a[i + 1])[-1] != '9'
    l2 = str(a[i])[-1] != '9' and str(a[i + 1])[-1] == '9'
    s2 = a[i] ** 2 + a[i + 1]**2
    if (l1 or l2) and s2 < m9**2:
        count += 1
        if s2 < sm:
            sm = s2
print(count, sm)


