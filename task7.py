temp = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
answer= []
for i in range(len(temp)):
    if(len(temp[i])!=0):
        answer.append(temp[i])
print(answer)