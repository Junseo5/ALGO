# 1946 . 간단한 압축 풀기

tc = int(input())

for T in range(tc):
    n = int(input())
    n_list = [input().split() for _ in range(n)]

    result = ''

    print(f"#{T + 1}")

    for i in n_list:
        for j in range(int(i[1])):
            if len(result) < 10:
                result += i[0]
            else:
                print(result)
                result = ''
                result += i[0]
    
    if result != '':
        print(result)