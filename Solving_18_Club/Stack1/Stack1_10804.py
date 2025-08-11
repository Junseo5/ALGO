# 10804 . 문자열의 거울상

# p, q, b, d 를 뒤집어서 출력

tc = int(input())

for T in range(tc):
    n_str = input()

    base_dict = {
        'b' : 'd',
        'p' : 'q',
        'd' : 'b',
        'q' : 'p',
    }

    n_list = list(reversed(n_str))

    for i in range(len(n_list)):
        n_list[i] = base_dict[n_list[i]]
    
    print(f"#{T + 1} {''.join(n_list)}")