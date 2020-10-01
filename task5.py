import math
ar = input().split()
base = []
answer = [base]

for i in range(len(ar)): 
    original = answer[:]
    new=ar[i]
    for j in range(len(answer)):
        answer[j] = answer[j]+ [new]
    answer = original + answer
for lists in answer:
    print(" ".join(lists))


    