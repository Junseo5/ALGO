# 9386 . 연속한 1의 개수

tc = int(input())

for T in range(tc):
    n = int(input())
    n_case = input()

    cnt = 0
    save_cnt = 0

    for i in range(len(n_case)):
        if n_case[i] == '1':
            cnt += 1
            
            if save_cnt < cnt:
                save_cnt = cnt
        else:
            cnt = 0
    
    print(f"#{T + 1} {save_cnt}")