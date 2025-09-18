# 1221 . [S/W 문제해결 기본] 5일차 - GNS

GNS_dict = {
        'ZRO' : 0,
        'ONE' : 1,
        'TWO' : 2,
        'THR' : 3,
        'FOR' : 4,
        'FIV' : 5,
        'SIX' : 6,
        'SVN' : 7,
        'EGT' : 8,
        'NIN' : 9,
    }

# 버블 정렬하니까 너무 느렸던 관계로 주석처리..
# def bubble_sort(arr):
#     global GNS_dict
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n-i-1):
#             if GNS_dict[arr[j]] > GNS_dict[arr[j+1]]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     return arr

def sort_gns(arr, mapping):
    return sorted(arr, key=lambda x: mapping[x])

tc = int(input())

for T in range(tc):
    case_num, n = input().split()
    GNS = input().split()

    print(f"#{T + 1}")
    print(*sort_gns(GNS, GNS_dict))
