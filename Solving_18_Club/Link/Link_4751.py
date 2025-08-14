# 4751 . 다솔이의 다이아몬드 장식

tc = int(input())

for T in range(tc):
    n_str = input()
    
    line_list1 = []
    line_list2 = []
    line_list3 = []
    line_list4 = []
    line_list5 = []
    
    for ch in n_str:
        line_list1.append('..#.')
        line_list2.append('.#.#')
        line_list3.append(f'#.{ch}.')
        line_list4.append('.#.#')
        line_list5.append('..#.')
    
    line_list1.append('.')
    line_list2.append('.')
    line_list3.append('#')
    line_list4.append('.')
    line_list5.append('.')
    
    p1 = ''.join(line_list1)
    p2 = ''.join(line_list2)
    p3 = ''.join(line_list3)
    p4 = ''.join(line_list4)
    p5 = ''.join(line_list5)
    
    print(f"{p1}\n{p2}\n{p3}\n{p4}\n{p5}")