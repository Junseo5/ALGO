# 2058. 자릿수 더하기

n = input()
sum = 0

for i in range(len(n)):
    sum += int(n[i])

print(sum)