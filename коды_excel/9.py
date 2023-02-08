file = open('9.txt')
count = 0
for line in file:
    alls = sorted(set([int(x) for x in line.split()]))
    if len(alls) == 3:
        s1 = alls[0] + alls[1]
        if alls[2] < s1:
            count += 1
print(count)

