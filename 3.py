string1 = input().split()
n = int(input())
n_perm = n
counter = len(string1)
c = 0
while counter > 0 :
    if n > len(string1) or c > len(string1):
        print(string1[len(string1)-counter:len(string1)])
    else:    
        print(string1[c:n])
        c+=n_perm
        n+=n_perm
    counter-=n_perm
