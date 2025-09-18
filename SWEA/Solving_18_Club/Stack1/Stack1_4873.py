# 4873 . [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기

# ABCCB 일 경우 반복 문자 CC를 지우고 BB를 붙인다
# ABB 에서 BB를 지우고 A만 남았으므로 1을 출력

tc = int(input())

for T in range(tc):
    n_list = list(input())
    
    while True:  # 다 지울때까지 반복
        is_val = False  # 한번이라도 지워졌는지 확인을 위한 bool 변수
        for i in range(1, len(n_list)):
            if n_list[i-1] == n_list[i]:  # 중복 두개 pop 시키고 다시 반복
                n_list.pop(i)
                n_list.pop(i-1)
                is_val = True
                break
        
        if not is_val:  # 지울게 없으면 퇴장
            break
    
    print(f"#{T + 1} {len(n_list)}")