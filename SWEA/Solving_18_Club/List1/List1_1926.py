# 1926 . 간단한 369게임

n = input()

for i in range(1, int(n) + 1):
    dash = False

    for j in range(len(str(i))):
        temp = str(i)
        if int(temp[j]) % 3 == 0 and int(temp[j]) != 0:
            print("-", end='')
            dash = True

    if not dash:
        print(i, end=' ')
    else:
        print(" ", end='')