# 1970 . 쉬운 거스름돈

# 우리나라 돈 기준 거스름돈 개수 책정기
# 5만 1만 5천 1천 500 100 50 10

coin_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

tc = int(input())

for T in range(tc):
    n = int(input())
    
    result_list = []
    
    for i in coin_list:
        result_list.append(str(n // i))
        n %= i
    
    print(f"#{T + 1}\n{' '.join(result_list)}")