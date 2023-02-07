a = '8' * 120
while '888' in a or '2222' in a:
    if '2222' in a:
        a = a.replace('2222', '88', 1)
    else:
        a = a.replace('888', '22', 1)
print(a.count('8'))