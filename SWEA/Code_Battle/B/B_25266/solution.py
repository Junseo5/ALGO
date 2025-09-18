# 25266 . 택시 호출 서비스

#####solution.py
from typing import List
from collections import defaultdict
import heapq

class Result:
    def __init__(self, mX, mY, mMoveDistance, mRideDistance):
        self.mX = mX
        self.mY = mY
        self.mMoveDistance = mMoveDistance
        self.mRideDistance = mRideDistance

def init(N : int, M : int, L : int, mXs : List[int], mYs : List[int]) -> None:
    global bucket, drive_total_dict, drive_user_dict, drive_distance_dict, id_dict, best_list, n, l

    n = N
    l = L
    bucket = [[defaultdict(list) for _ in range(10)] for _ in range(10)]
    drive_total_dict = defaultdict(int)
    drive_user_dict = defaultdict(int)
    drive_distance_dict = defaultdict(list)
    id_dict = {}

    # 버킷 10 * 10에 각 딕셔너리를 n / 10 이후 차례대로 추가
    # x y좌표를 x에 10만 곱하고 y를 더함 ex) 2, 1 -> 200001
    # 해당 값을 키로 가지고
    # x // (n // 10) 이 값의 인덱스에 딕셔너리 추가 3560 // 1000 = 3

    for i in range(M):
        x = mXs[i]
        y = mYs[i]
        bucket[x // (n // 10)][y // (n // 10)][(x * 100000) + y].append(i + 1)
        id_dict[i + 1] = (x, y)


def pickup(mSX : int, mSY : int, mEX : int, mEY : int) -> int:
    # 출발지 좌표가 포함된 버킷을 찾고, 해당 버킷의 주변 8블럭을 탐색
    # 내 좌표와 가장 가까운 주변 블럭 안에 해당 값이 있는지 확인

    def find_pickup(x, y):  # 버킷 기준 x, y값 전달, 택시와의 거리 반환
        bucket_list = []
        for loc, _ in bucket[x][y].items():
            loc_x = loc // 100000
            loc_y = loc % 100000

            distance = abs(loc_x - mSX) + abs(loc_y - mSY)

            heapq.heappush(bucket_list, (distance, loc))

        hq_list = []
        hq_list.append(heapq.heappop(bucket_list))
        temp = hq_list[0][0]

        if bucket_list:
            i = 0
            while hq_list[i][0] == temp and bucket_list:
                hq_list.append(heapq.heappop(bucket_list))
                i += 1
            hq_list.pop()

        return hq_list


    # temp_unpack_dict = {}

    # mSXY = (mSX * 100000) + mSY

    # if mSXY in bucket[mSX // (n // 10)][mSY // (n // 10)]:
    # temp_unpack_dict.update(bucket[mSX // (n // 10)][mSY // (n // 10)])
    find_list = []
    bucket_x = mSX // (n // 10)
    bucket_y = mSY // (n // 10)

    if bucket[bucket_x][bucket_y]:
        find_list.extend(find_pickup(bucket_x, bucket_y))

    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]

    for dx, dy in dxy:
        x = bucket_x + dx
        y = bucket_y + dy
        # temp_unpack_dict.update(bucket[x // (n // 10)][y // (n // 10)])

        if 0 <= x < 10 and 0 <= y < 10:
            if bucket[x][y]:
                find_list.extend(find_pickup(x, y))

    if not find_list:
        return -1

    heapq.heapify(find_list)
    find_hq = []
    find_hq.append(heapq.heappop(find_list))
    temp = find_hq[0][0]

    if find_list:
        i = 0
        while find_hq[i][0] == temp and find_list:
            find_hq.append(heapq.heappop(find_list))
            i += 1
        find_hq.pop()

    if find_hq[0][0] > l:  # 거리가 L 초과면 -1 반환
        return -1

    find2_list = []
    for distance, loc in find_hq:
        loc_x = loc // 100000
        loc_y = loc % 100000
        id_list = bucket[loc_x // (n // 10)][loc_y // (n // 10)][loc]
        heapq.heappush(find2_list, (min(id_list), loc, distance))

    id, loc, distance = heapq.heappop(find2_list)

    if len(bucket[loc_x // (n // 10)][loc_y // (n // 10)][loc]) > 1:
        del_idx = bucket[loc_x // (n // 10)][loc_y // (n // 10)][loc].index(id)
        bucket[loc_x // (n // 10)][loc_y // (n // 10)][loc].pop(del_idx)
    else:
        del bucket[loc_x // (n // 10)][loc_y // (n // 10)][loc]

    bucket[mEX // (n // 10)][mEY // (n // 10)][(mEX * 100000) + mEY].append(id)

    loc_x = loc // 100000
    loc_y = loc % 100000
    distance_user = abs(mEX - loc_x) + abs(mEY - loc_y)
    distance += distance_user

    drive_total_dict[id] += distance
    drive_user_dict[id] += distance_user
    id_dict[id] = (mEX, mEY)

    if drive_user_dict[id] != distance_user:
        if len(drive_distance_dict[-(drive_user_dict[id] - distance_user)]) > 1:
            del_idx = drive_distance_dict[-(drive_user_dict[id] - distance_user)].index(id)
            drive_distance_dict[-(drive_user_dict[id] - distance_user)].pop(del_idx)
        else:
            del drive_distance_dict[-(drive_user_dict[id] - distance_user)]

    drive_distance_dict[-(drive_user_dict[id])].append(id)


    return id


def reset(mNo : int) -> Result:
    total = drive_total_dict[mNo]
    user = drive_user_dict[mNo]

    drive_total_dict[mNo] = 0
    drive_user_dict[mNo] = 0

    if drive_distance_dict.get(-(user)) != None:
        if mNo in drive_distance_dict[-(user)]:
            del_idx = drive_distance_dict[-(user)].index(mNo)
            drive_distance_dict[-(user)].pop(del_idx)

    return Result(id_dict[mNo][0], id_dict[mNo][1], total, user)


def getBest(mNos : List[int]) -> None:
    drive_distance_dict[0] = [1, 2, 3, 4, 5]
    hq_list = list(drive_distance_dict)

    heapq.heapify(hq_list)

    top_list = []

    for _ in range(len(hq_list)):
        hq = heapq.heappop(hq_list)
        key_sort_list = sorted(drive_distance_dict[hq])
        for key in key_sort_list:
            if key not in top_list:
                top_list.append(key)
            if len(top_list) == 5:
                break
        if len(top_list) == 5:
            break

    mNos.extend([
        top_list[0],
        top_list[1],
        top_list[2],
        top_list[3],
        top_list[4]
    ])

    del drive_distance_dict[0]




# # 25266 . 택시 호출 서비스
#
# #####solution.py
# from typing import List
# from collections import defaultdict
#
#
# class Result:
#     def __init__(self, mX, mY, mMoveDistance, mRideDistance):
#         self.mX = mX
#         self.mY = mY
#         self.mMoveDistance = mMoveDistance
#         self.mRideDistance = mRideDistance
#
#
# N_val, L_val, M_val = 0, 0, 0
# taxi_locations = {}  # { taxi_id: (x, y) }
# bucket = None  # bucket[bx][by] = { (x,y): {taxi_id1, taxi_id2} }
# total_move_dist = None  # { taxi_id: distance }
# ride_dist = None  # { taxi_id: distance }
# dist_to_taxis = None  # { -ride_dist: {taxi_id1, taxi_id2} }
#
#
# def init(N: int, M: int, L: int, mXs: List[int], mYs: List[int]) -> None:
#     global N_val, L_val, M_val, taxi_locations, bucket, total_move_dist, ride_dist, dist_to_taxis
#
#     N_val = N
#     L_val = L
#     M_val = M
#
#     bucket_size = N // 10
#     bucket = [[defaultdict(set) for _ in range(10)] for _ in range(10)]
#     taxi_locations = {}
#     total_move_dist = defaultdict(int)
#     ride_dist = defaultdict(int)
#     dist_to_taxis = defaultdict(set)
#
#     initial_taxis = set()
#     for i in range(M):
#         taxi_id = i + 1
#         x, y = mXs[i], mYs[i]
#
#         taxi_locations[taxi_id] = (x, y)
#         bx, by = x // bucket_size, y // bucket_size
#         bucket[bx][by][(x, y)].add(taxi_id)
#
#         initial_taxis.add(taxi_id)
#
#     dist_to_taxis[0] = initial_taxis
#
#
# def pickup(mSX: int, mSY: int, mEX: int, mEY: int) -> int:
#     bucket_size = N_val // 10
#
#     candidates = []
#     start_bx, start_by = mSX // bucket_size, mSY // bucket_size
#
#     for i in range(start_bx - 1, start_bx + 2):
#         for j in range(start_by - 1, start_by + 2):
#             if not (0 <= i < 10 and 0 <= j < 10):
#                 continue
#
#             for (tx, ty), taxi_ids in bucket[i][j].items():
#                 dist = abs(mSX - tx) + abs(mSY - ty)
#                 if dist <= L_val:
#                     for taxi_id in taxi_ids:
#                         candidates.append((dist, taxi_id))
#
#     if not candidates:
#         return -1
#
#     pickup_dist, best_taxi_id = min(candidates)
#
#     old_tx, old_ty = taxi_locations[best_taxi_id]
#     old_bx, old_by = old_tx // bucket_size, old_ty // bucket_size
#
#     bucket[old_bx][old_by][(old_tx, old_ty)].remove(best_taxi_id)
#     if not bucket[old_bx][old_by][(old_tx, old_ty)]:
#         del bucket[old_bx][old_by][(old_tx, old_ty)]
#
#     taxi_locations[best_taxi_id] = (mEX, mEY)
#     new_bx, new_by = mEX // bucket_size, mEY // bucket_size
#     bucket[new_bx][new_by][(mEX, mEY)].add(best_taxi_id)
#
#     old_ride = ride_dist[best_taxi_id]
#     dist_to_taxis[-old_ride].remove(best_taxi_id)
#     if not dist_to_taxis[-old_ride]:
#         del dist_to_taxis[-old_ride]
#
#     customer_dist = abs(mSX - mEX) + abs(mSY - mEY)
#     total_move_dist[best_taxi_id] += pickup_dist + customer_dist
#     ride_dist[best_taxi_id] += customer_dist
#
#     new_ride = ride_dist[best_taxi_id]
#     dist_to_taxis[-new_ride].add(best_taxi_id)
#
#     return best_taxi_id
#
#
# def reset(mNo: int) -> Result:
#     cur_x, cur_y = taxi_locations[mNo]
#     move_dist = total_move_dist[mNo]
#     rd_dist = ride_dist[mNo]
#
#     dist_to_taxis[-rd_dist].remove(mNo)
#     if not dist_to_taxis[-rd_dist]:
#         del dist_to_taxis[-rd_dist]
#
#     total_move_dist[mNo] = 0
#     ride_dist[mNo] = 0
#
#     dist_to_taxis[0].add(mNo)
#
#     return Result(cur_x, cur_y, move_dist, rd_dist)
#
#
# def getBest(mNos: List[int]) -> None:
#     top_taxis = []
#
#     sorted_dists = sorted(dist_to_taxis.keys())
#
#     for dist_key in sorted_dists:
#         taxis_at_dist = sorted(list(dist_to_taxis[dist_key]))
#         for taxi_id in taxis_at_dist:
#             top_taxis.append(taxi_id)
#             if len(top_taxis) == 5:
#                 break
#         if len(top_taxis) == 5:
#             break
#
#     for i in range(5):
#         mNos[i] = top_taxis[i]