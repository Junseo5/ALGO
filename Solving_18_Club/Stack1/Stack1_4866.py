# 4866 . [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사

# 여는 괄호가 나오면 append
# 리스트가 비어있지 않고 닫는 괄호가 나오면 pop으로 비교
# 다르면 0 같으면 계속

tc = int(input())

for T in range(tc):
    codes = input()  # 코드들 받음

    base_dict = {  # 닫힌괄호를 기준으로 비교하기에 키값은 닫힌 괄호
        ')' : '(',
        '}' : '{',
        ']' : '[',
    }

    # 1 혹은 0 저장할 is_val 선언 및 괄호 저장용 리스트
    save_list = []
    is_val = 1

    for i in codes:  # 모든값 순회
        if i in base_dict.values():  # 딕셔너리 밸류값 열린괄호가 있으면 append
            save_list.append(i)
        
        if i in base_dict.keys():  # 딕셔너리 키값 닫힌괄호가 있으면 진입
            if not save_list:  # 닫힌괄호 나왔는데 저장된 열린괄호 없으면 퇴장 후 0 출력
                is_val = 0
                break
            if save_list[-1] == base_dict[i]:  # 마지막 저장된 열린괄호와 딕셔너리 닫힌값의 밸류값이 같으면 정상
                is_val = 1
                save_list.pop()  # 정상 괄호 확인되었으므로 저장된 열린 괄호 제거
            else:  # 마지막 괄호와 대칭되지 않은 경우 퇴장 후 0 출력
                is_val = 0
                break
    
    if save_list:  # 마지막까지 저장된 괄호가 있을 경우 0 출력
        is_val = 0
    
    print(f"#{T + 1} {is_val}")