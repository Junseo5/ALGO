# 1223 . [S/W 문제해결 기본] 6일차 - 계산기1

for T in range(10):
    n_len = int(input())
    n = input().strip()

    stack = []
    postfix = []

    for i in n:
        if i.isnumeric():
            postfix.append(i)
        
        else:
            if stack:
                postfix.append(stack.pop())
            
            stack.append(i)
        
    while stack:
        postfix.append(stack.pop())
    
    for i in postfix:
        if i.isnumeric():
            stack.append(int(i))
        
        else:
            number2 = stack.pop()
            number1 = stack.pop()

            if i == '+':
                stack.append(number1 + number2)
            else:
                print("+ 연산자가 아닙니다.")
    
    print(f"#{T + 1} {stack.pop()}")