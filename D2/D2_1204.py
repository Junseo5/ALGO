# 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기

tc = int(input())

for T in range(tc):
    c = int(input())
    n = list(map(int, input().split()))

    n_set = set(n)

    result_cnt = 0
    result_score = 0

    for i in n_set:
        cnt = 0
        for j in range(len(n)-1, -1, -1):
            if i == n[j]:
                n.pop(j)
                cnt += 1
        if result_cnt < cnt:
            result_score = i
            result_cnt = cnt
        elif result_cnt == cnt:
            if result_score < i:
                result_score = i
                result_cnt = cnt

    print(f"#{T+1} {result_score}")

# 테스트 케이스 밑에 또 테스트 케이스 번호가 나오는 문제는 처음 봤다
# 편하게 구현하려다 보니 set으로 숫자 중복제거하여 모든 숫자 1번씩 순회하며
# 그래도 좀 빨리 돌아가라고 pop 사용하여 이미 계산한 값은 삭제시키며 순회시켰다.
# pop 이용한 반복문은 인덱스 이슈로 for문을 리버스 해서 돌려야 한다.