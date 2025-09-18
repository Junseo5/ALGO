# 6485 . 삼성시의 버스 노선

# 입력
# 테스트 케이스 개수 T
# 버스 노선 n (n개만큼 a, b 입력 받음)
# a이상 b이하 노선만 다닌다. ex) 1~3
# 다음 p를 입력받고 ex) 5
# 입력받은 p 만큼 정류장 번호를 하나씩 입력받음(c1, c2, c3, c4, c5)
# 정리
# 입력받은 노선 1~3이랑 2~5인 경우
# c1부터 c5 차례로 1 2 3 4 5 가정했을 때
# 겹치는 개수를 출력
# 출력 ex) #1 1 2 2 1 1
# 1~3과 2~5는 2~3이 겹치므로 2번, 3번만 2로 출력

# 테스트 케이스 입력
tc = int(input())

# 테스트 케이스 순회
for T in range(tc):
    # n 을 단순 int()감싸서 입력
    # n_list 로 이중 리스트로 a, b를 n만큼 입력 받음
    # p 를 단순 int()감싸서 입력받음
    # c_dict 빈 딕셔너리 선언, p만큼 for문 생성
    # c_dict[int(input())] = 0

    # 딕셔너리로 구상했지만 순서를 보장하지 못해 오류 발생
    # 리스트로 변경하여 재구현
    n = int(input())
    n_list = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())
    c_list = [int(input()) for _ in range(p)]

    base_list = [0] * p

    # for문 i를 n만큼, j를 n_list[i][0]부터 [1]까지
    # j 돌면서 만약 현재값이 c_dict에 있으면
    # c_dict[j] += 1
    for i in range(n):
        a, b = n_list[i]
        for j in range(p):
            if a <= c_list[j] <= b:
                base_list[j] += 1
                
    
    result = ' '.join(list(map(str, base_list)))
    print(f"#{T + 1} {result}")