# 4013 . [모의 SW 역량테스트] 특이한 자석

from collections import deque

tc = int(input())

for T in range(tc):
    k = int(input())
    magnet_list = [deque(map(int, input().split())) for _ in range(4)]
    k_info_list = [tuple(map(int, input().split())) for _ in range(k)]
    
    for mag_num, rot in k_info_list:
        rot_mag = [0] * 4
        rot_mag[mag_num - 1] = rot

        for i in range(mag_num - 1, 0, -1):
            if magnet_list[i][6] != magnet_list[i-1][2]:
                rot_mag[i-1] = -rot_mag[i]
            else:
                break

        for i in range(mag_num - 1, 3):
            if magnet_list[i][2] != magnet_list[i+1][6]:
                rot_mag[i+1] = -rot_mag[i]
            else:
                break

        for i in range(4):
            if rot_mag[i] != 0:
                magnet_list[i].rotate(rot_mag[i])
    
    total = (magnet_list[0][0] * 1) + (magnet_list[1][0] * 2) + (magnet_list[2][0] * 4) + (magnet_list[3][0] * 8)
    
    print(f"#{T + 1} {total}")
