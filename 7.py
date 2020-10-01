a =  [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
b = []
for i in a:
    if len(i)!=0:
        b.append(i)
print(b)
