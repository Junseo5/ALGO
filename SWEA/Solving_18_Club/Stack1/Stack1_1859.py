# 1859 . 백만 장자 프로젝트

# 입력으로 매매가 들어옵니다.
# 일일 구매 개수 제한이 있음
# 예를들어 3일동안 1, 2, 3 매매가 들어오면
# 앞 두날에 구매 후 마지막날에 판매하여 3 이득

# 뒤에서부터 카운트하여 앞에가 더 작을 때까지 반복

tc = int(input())

for T in range(tc):
    n = int(input())
    n_list = list(map(int, input().split()))

    cnt = 0
    temp_max_money = 0

    for i in range(n-1, 0, -1):  # 앞 인덱스 비교로 인해 앞에서 두번째까지만 반복
        temp_max_money = max(temp_max_money, n_list[i])
        
        if n_list[i - 1] < temp_max_money:
            cnt += temp_max_money - n_list[i - 1]
    
    print(f"#{T + 1} {cnt}")