# 6320. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 2

ni = input()
mi = input()
n = input()
m = input()

if (n == "가위" and m == "바위") or (m == "가위" and n == "바위"):
    print("바위가 이겼습니다!")
elif (n == "보" and m == "바위") or (m == "보" and n == "바위"):
    print("보가 이겼습니다!")
elif (n == "가위" and m == "보") or (m == "가위" and n == "보"):
    print("가위가 이겼습니다!")
    
# 이름 입력받고 아무것도 안하는 문제..?