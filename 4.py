string1 = input().split()
a = []
for i in string1:
    if i in string1 and i not in a:
        a.append(i)
print(*a)
