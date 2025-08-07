# 1974 . # 스도쿠 검증

# 스도쿠는 1부터 9까지 중복값이 없다는 점
# 1회 반복으로 set()함수 사용하여 중복값 제거
# 이후 길이가 9인지 확인
# 9가 맞으면 다음 9가 아니면 break 후 0출력
# 다음은 i 0~9까지 3칸씩 j 3칸씩 반복하여 3칸씩 슬라이싱
# 이후 set()

tc = int(input())

for T in range(tc):
    n = 9
    n_list = [list(map(int, input().split())) for _ in range(n)]

    result = 1

    for i in range(n):
        temp = [n_list[x][i] for x in range(n)]

        if len(set(n_list[i])) != 9 or len(set(temp)) != 9:
            result = 0
            break

    for i in range(0, n, 3):
        if result == 0:
            break

        for j in range(0, n, 3):
            block_set = set(n_list[i][j:j+3]).union(set(n_list[i+1][j:j+3]), set(n_list[i+2][j:j+3]))

            if len(block_set) != 9:
                result = 0
                break

    print(f"#{T + 1} {result}")