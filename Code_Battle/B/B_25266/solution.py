# 25266 . 택시 호출 서비스

#####solution.py
from typing import List
from collections import defaultdict

class Result:
    def __init__(self, mX, mY, mMoveDistance, mRideDistance):
        self.mX = mX
        self.mY = mY
        self.mMoveDistance = mMoveDistance
        self.mRideDistance = mRideDistance

def init(N : int, M : int, L : int, mXs : List[int], mYs : List[int]) -> None:
    global bucket, n, l, mxs, mys

    n = N
    l = L
    mxs = mXs
    mys = mYs
    bucket = [[defaultdict(list) for _ in range(10)] for _ in range(10)]
    
    # 버킷 10 * 10에 각 딕셔너리를 n / 10 이후 차례대로 추가
    # x y좌표를 x에 10만 곱하고 y를 더함 ex) 2, 1 -> 200001
    # 해당 값을 키로 가지고
    # x // (n // 100) 이 값의 인덱스에 딕셔너리 추가 356 // 100 = 3

    for i in range(M):
        x = mxs[i]
        y = mys[i]
        bucket[x // (n // 100)][y // (n // 100)][(x * 100000) + y].append(i)
    


def pickup(mSX : int, mSY : int, mEX : int, mEY : int) -> int:
    # 출발지 좌표가 포함된 버킷을 찾고, 해당 버킷의 주변 8블럭을 탐색
    # 내 좌표와 가장 가까운 주변 블럭 안에 해당 값이 있는지 확인

    def find_pickup(x, y):
        bucket[x // (n // 100)][y // (n // 100)]
        


    # temp_unpack_dict = {}

    # mSXY = (mSX * 100000) + mSY

    # if mSXY in bucket[mSX // (n // 100)][mSY // (n // 100)]:
    # temp_unpack_dict.update(bucket[mSX // (n // 100)][mSY // (n // 100)])
    find_pickup(mSX, mSY)

    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]

    for dx, dy in dxy:
        x = mSX + dx
        y = mSY + dy
        # temp_unpack_dict.update(bucket[x // (n // 100)][y // (n // 100)])

        find_pickup(x, y)
    


    return -1

def reset(mNo : int) -> Result:
    return Result(-1, -1, -1, -1)

def getBest(mNos : List[int]) -> None:
    pass

