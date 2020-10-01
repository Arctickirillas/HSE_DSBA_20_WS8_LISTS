string =  input().split()
base = []   
lists = [base] 
for i in range(len(string)): 
    orig = lists[:]
    new = string[i] 
    for j in range(len(lists)): 
        lists[j] = lists[j] + [new] 
    lists = orig + lists
print(lists)
