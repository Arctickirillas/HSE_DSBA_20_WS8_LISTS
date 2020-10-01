import math
text = input().split()
n = int(input())
answer = []
for i in range(math.ceil(len(text)/n)):
    answer.append(text[:n])
    text=text[n:]
print(answer)
