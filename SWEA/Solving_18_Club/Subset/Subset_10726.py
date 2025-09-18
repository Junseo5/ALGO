# 10726 . 이진수 표현

total_list = []

tc = int(input())

for T in range(tc):
    n, m = map(int, input().split())

    m_origin_list = str(bin(m))
    m_list = m_origin_list[-n:]

    result = 'ON'

    if '0' in m_list or 'b' in m_list:
        result = 'OFF'

    total_list.append(f"#{T + 1} {result}\n")


print(''.join(total_list))