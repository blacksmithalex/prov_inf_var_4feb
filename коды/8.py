def f(n):
    for i in range(len(n) - 1):
        if (int(n[i]) + int(n[i + 1])) % 2 == 0:
            return False
    return True

nums = list('0123456')
count = 0
for a1 in nums[1:]:
    for a2 in nums:
        for a3 in nums:
            for a4 in nums:
                for a5 in nums:
                    for a6 in nums:
                        a = a1 + a2 + a3 + a4 + a5 + a6
                        if f(a) and a.count('6') == 1:
                            count += 1
print(count)

