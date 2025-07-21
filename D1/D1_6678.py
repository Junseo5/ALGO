# 6678. [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 4. 문자열 4

stack = []

while True:
    try:
        random = input()
        if not random:
            break
        stack.append(random.upper())
    except:
        break

for i in range(len(stack)):
    print(f">> {stack[i]}")

# SWEA와 같은 곳에서는 try-except로 오류가 날 것 같은 코드에 감싸주면 잘 돌아간다.