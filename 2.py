string1 = input().split()
string2 = input().split()
a = []
b = []
for i in string1:
    if i in string1 and i not in a:
        a.append(i)
for j in string2:
    if j in string2 and j not in b:
        b.append(j)
if sorted(b) == sorted(a):
    print('YES')
else:
    print('NO')
