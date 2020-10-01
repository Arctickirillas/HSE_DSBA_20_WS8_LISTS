a = list(map(int, input().split()))
from1 = []
ans = [from1]
for i in range(len(a)):
    orig = ans[:]
    next1 = a[i]
    for j in range(len(ans)):
        ans[j] = ans[j] + [next1]
    ans = orig + ans
for i in ans:
    if i != []:
        print(*i)
