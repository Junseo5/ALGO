# 1223 . [S/W 문제해결 기본] 6일차 - 계산기2

for T in range(10):
    n_len = int(input())
    n = input().strip()

    op_dict = {
        '(' : 0,
        '+' : 1,
        '-' : 1,
        '*' : 2,
        '/' : 2,
    }

    stack = []
    postfix = []

    for i in n:
        # i가 숫자면 True
        if i.isnumeric():
            postfix.append(i)
        
        elif i == '(':
            stack.append(i)
        
        elif i == ')':
            temp = stack.pop()
            
            while temp != '(':
                postfix.append(temp)
                temp = stack.pop()
        
        # op_dict[i]현재값과 op_dict[stack[-1]]마지막 값 비교
        # 기존값이 더 크거나 같으면 기존값 pop 후 postfix에 추가 후 다시 검사
        # 현재값이 더 크면 나와서 stack에 append
        else:
            while stack and op_dict[i] <= op_dict[stack[-1]]:
                temp = stack.pop()
                postfix.append(temp)
            
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
            elif i == '-':
                stack.append(number1 - number2)
            elif i == '*':
                stack.append(number1 * number2)
            elif i == '/':
                stack.append(number1 / number2)
    
    print(f"#{T + 1} {stack.pop()}")