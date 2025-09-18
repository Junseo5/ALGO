# 10912. 외로운 문자

from collections import Counter

result_list = []

tc = int(input())

for T in range(tc):
    n_dict = Counter(input())
    
    stack_list = []
    for ch, cnt in n_dict.items():
        if cnt % 2 == 1:
            stack_list.append(ch)
    
    if not stack_list:
        stack_list.append('Good')
    
    stack_list.sort()
    
    result_list.append(f"#{T + 1} {''.join(stack_list)}\n")

print(''.join(result_list))