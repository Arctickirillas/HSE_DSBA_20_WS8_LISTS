a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
ans = 'YES'
for i in a:
    if i not in c:
        c.append(i)
for i in b:
    if i not in c:
        ans = 'NO'
        break
print(ans)
