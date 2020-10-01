ar1 = []
ar2=[]
ar1 = input().split()
ar2 =  input().split()
flag = True
for number in ar1:
    if(number in ar2):
        continue
    else:
        flag = False
for number in ar2:
    if(number in ar1):
        continue
    else:
        flag = False

if(flag):
    print("YES")
else:
    print("NO")
