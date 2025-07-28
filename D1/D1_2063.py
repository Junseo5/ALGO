# 2063. 중간값 찾기

n = int(input())
score = list(map(int, input().split()))

score = list(set(score))
score.sort()
print(score[(len(score)//2)+1])