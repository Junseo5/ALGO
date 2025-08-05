# 11092 . 최대 최소의 간격

tc = int(input())

for T in range(tc):
    n = int(input())
    num_list = list(map(int, input().split()))

    min_num = num_list.index(min(num_list))
    max_num = (n - 1) - num_list[::-1].index(max(num_list))  # 뒤에서부터 인덱스 번호 찾음 0인경우 마지막 인덱스

    print(f"#{T + 1} {abs(max_num - min_num)}")
    