# 6019 . 기차 사이의 파리

result_list = []

tc = int(input())

for T in range(tc):
    d, a, b, f = map(int, input().split())

    total = f * (d / (a + b))
    
    result_list.append(f"#{T + 1} {total}\n")
    
print(''.join(result_list))
