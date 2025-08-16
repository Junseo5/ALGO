# 9280 . 진용이네 주차타워

# in_out_list로 들어오는건 parking_list로 넣고 꽉차면 대기
# 가장 빠른 음수 찾아서 없애고 다시 순회
# 0보다 작으면 abs 절대값 변환 후 같은값 parking_list 탐색

tc = int(input())

for T in range(tc):
    n, m = map(int, input().split())
    r_list = [int(input()) for _ in range(n)]
    w_list = [int(input()) for _ in range(m)]
    in_out_list = [int(input()) for _ in range(m * 2)]
    
    parking_list = [0] * n
    total_money = 0
    
    for i in range(len(in_out_list)):
        if (in_out_list[i] > 0) and (0 not in parking_list):
            for j in range(i, len(in_out_list)):
                if (in_out_list[j] < 0) and (abs(in_out_list[j]) in parking_list):
                    parking_list[parking_list.index(abs(in_out_list[j]))] = 0
                    break
        
        elif (in_out_list[i] < 0) and (abs(in_out_list[i]) not in parking_list):
            continue
        
        try:  # 메인 계산식
            if in_out_list[i] < 0:
                parking_list[parking_list.index(abs(in_out_list[i]))] = 0
                continue
            
            temp_idx = parking_list.index(0)
            parking_list[temp_idx] = in_out_list[i]
            total_money += r_list[temp_idx] * (w_list[in_out_list[i] - 1])
            
        except:
            print("인덱스 오류")
    
    print(f"#{T + 1} {total_money}")