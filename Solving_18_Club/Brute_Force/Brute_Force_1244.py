# 1244 . [S/W 문제해결 응용] 2일차 - 최대 상금

# 순열 후 k개 만큼 바뀐 값들만 저장 후 max값 출력

tc = int(input())

for T in range(tc):
    n_str, k = input().split()
    n_list = set(n_str)
    size = len(n_str)

    for _ in range(int(k)):
        temp_set = set()
        arr = list(n_list)
        for i in range(size - 1):
            for j in range(i + 1, size):
                arr[i], arr[j] = arr[j], arr[i]
                temp_set.add(''.join(arr))
                arr[i], arr[j] = arr[j], arr[i]
        n_list = temp_set

    print(max(map(int, n_list)))


    # n_set = set(n_list)
    # n_same_list = []
    # for i in n_list:
    #     if i in n_set:
    #         if n_list.count(i) > 1:
    #             n_same_list.append(i)
    #
    # n_per = itertools.permutations(n_list)
    #
    # save_list = []
    #
    # for i in n_per:
    #     cnt = 0
    #
    #     for j in range(size):
    #         if n_list[j] == i[j] and i[j] in n_same_list:
    #
    #
    #     for j in range(k):
    #
    #
    #     if cnt // 2 == k:
    #         save_list.append(int(''.join(map(str, i))))
    #
    # print(f"#{T + 1} {max(save_list)}")