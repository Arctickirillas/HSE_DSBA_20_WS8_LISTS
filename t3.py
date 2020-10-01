a = input().split()
b = int(input())
z = 0
while True:
    print(*a[z:z+b])
    if z + b >= len(a):
        break
    else:
        z = z+b