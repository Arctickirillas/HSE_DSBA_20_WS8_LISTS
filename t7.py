a = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
c = []
for i in a:
    if i != ():
        c.append(i)
print(c)
