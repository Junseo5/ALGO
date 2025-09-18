# 5432 . 쇠막대기 자르기

# 열림 괄호는 stack.append 시켜놓고 닫힌괄호 나오면 레이저인지 확인
# 레이저인 경우 마지막 열린괄호 pop 시키고 남은 열린괄호 개수만큼 기존값에 더함
# 그리고 레이저가 아닌 닫힌 괄호가 나오면 마지막 열린괄호 pop 이후 기존값 +1

# tc = int(input())

# for T in range(tc):
#     n_str = input()
    
#     stack = []
#     cnt = 0
#     open_cnt = 0
    
#     for i in n_str:
#         if i == '(':
#             stack.append(i)
#             open_cnt += 1
        
#         elif i == ')':
#             if stack[-1] == '(':
#                 stack.pop()
#                 open_cnt -= 1
#                 cnt += open_cnt
#                 stack.append('O')  # 레이저 균형 맞추기 append
            
#             else:
#                 for j in range(len(stack)-1, -1, -1):
#                     if stack[j] == '(':
#                         stack.pop(j)
#                         open_cnt -= 1
#                         cnt += 1
#                         break
    
#     print(f"#{T + 1} {cnt}")

tc = int(input())

for T in range(tc):
    n_str = input()
    
    temp = ''
    cnt = 0
    open_cnt = 0
    
    for i in n_str:
        if i == '(':
            open_cnt += 1
        
        elif i == ')':
            if temp == '(':
                open_cnt -= 1
                cnt += open_cnt
            
            else:
                open_cnt -= 1
                cnt += 1
        temp = i
    
    print(f"#{T + 1} {cnt}")