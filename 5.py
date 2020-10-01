string =  input().split() 
lists = [[]] 
for i in range(len(string)): 
    orig = lists[:]
    new_list = string[i] 
    for j in range(len(lists)): 
        lists[j] = lists[j] + [new_list] 
    lists = orig + lists
print(lists)
