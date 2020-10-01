a = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
c = []
for i in range(len(a)):
    c.append(a[i][0:-1]+(100,))
print(c)
