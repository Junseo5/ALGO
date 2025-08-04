# 4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드

tc = int(input())

for T in range(tc):
    n = int(input())
    cards = sorted(input(), reverse=True)

    cards_dict = {}

    for i in range(len(cards)):
        try:
            cards_dict[int(cards[i])] += 1
        except:
            cards_dict[int(cards[i])] = 1
    
    cards_list = sorted(cards_dict, key=lambda x: cards_dict[x], reverse=True)
    
    print(f"#{T + 1} {cards_list[0]} {cards_dict[cards_list[0]]}")

# 시간복잡도는 내다버린 코드다.