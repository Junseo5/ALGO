# 2005 . 파스칼의 삼각형

# 크기 n 파스칼 삼각형
# 첫번째 줄은 항상 숫자 1이다
# 두번째 줄부터 각 숫자들은 자신의 왼쪽, 오른쪽 위의 숫자의 합이다

tc = int(input())

for T in range(tc):
    n = int(input())

    save_list = [[1]]
    str_list = ['1']

    for i in range(1, n):
        save_list.append([save_list[0][0]])
        for j in range(1, i):
            save_list[i].extend([save_list[i - 1][j - 1] + save_list[i - 1][j]])
        
        save_list[i].extend([save_list[0][0]])
        str_list.append(' '.join(list(map(str, save_list[i]))))

    finish = '\n'.join(str_list)
    print(f"#{T + 1}\n{finish}")
