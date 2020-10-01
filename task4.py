stroka = input().split()
answer = []
for i in range(len(stroka)):
    if(stroka[i] in answer):
        continue
    else:
        answer.append(stroka[i])
print(" ".join(answer))