kort = [(10,20,50), (40,50,60), (70,80,90)]
for i in range(len(kort)):
    temp = list(kort[i])
    temp[len(temp)-1]=1000
    kort[i]=temp
print(kort)