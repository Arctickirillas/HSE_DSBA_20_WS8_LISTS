s=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
q=[]

for i in range(len(s)):
    w=list(s[i])
    if w!=[]:
        q.append(tuple(w))
print(q)
    
