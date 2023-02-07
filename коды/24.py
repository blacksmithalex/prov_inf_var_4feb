file = open('24.txt')
a = file.readline()
file.close()

a = a.replace('BBA', 'X')
a = a.replace('CCA', 'X')
a = a.replace('BCA', 'X')
a = a.replace('CBA', 'X')

count, countm = 0, 0
for x in a:
    if x == 'X':
        count += 1
        if count > countm:
            countm = count
    else:
        count = 0
print(countm * 3 )