#####solution.py

# 인기검색어

# 모든 값을 deque 리스트에 저장
# 만번 호출되는 함수에서는 단순 저장만
# 계산은 100번 호출되는 순위 출력에서만

from typing import List
from collections import deque, defaultdict, Counter

# def init(N : int) -> None:
def init(N):
    global n, dq_list
    n = N
    dq_list = deque()


# def addKeyword(mKeyword : str) -> None:
def addKeyword(mKeyword):
    if len(dq_list) >= n:
        dq_list.popleft()
    
    dq_list.append(mKeyword)


# def top5Keyword(mRet : List[str]) -> int:
def top5Keyword(mRet):
    # mRet에 인기 검색어 최대 5개를 저장한다.
    # 반환은 mRet에 저장된 개수이다.
    # mRet은 우선순위가 높은 순으로 저장하라

    # 중복 제거를 위해 dq_list 통으로 set
    # 남은 값만 유사어 비교 후 각 유사어 리스트에 추가
    # 추가된 유사어 각 dq_list.count() 하여 개수 확인
    # 개수 같은 경우 문자값 비교 후 더 작은 값을 대표로 추가
    

    dq_set_list = set(dq_list)
    save_list = []

    # for i in dq_set_list:
    #     for j in dq_set_list:
    #         # 문자열 길이가 같지 않을 경우 유사어 아님
    #         if len(i) != len(j):
    #             continue
    #         cnt = 0
    #         # 길이가 같은 문자열 두개를 한단어씩 비교
    #         for ch1, ch2 in zip(i, j):
    #             if ch1 != ch2:
    #                 cnt += 1
    #                 if cnt > 1:
    #                     break
    

    same_len_dict = defaultdict(list)
    same_list = []

    for i in dq_set_list:
        same_len_dict[len(i)].append(i)

    for i in same_len_dict.values():
        same_dict = defaultdict(list)

        for j in i:
            for k in range(len(j)):
                temp = j[:k] + '@' + j[k+1:]
                same_dict[temp].append(j)
        
        for origin, same in same_dict.items():
            if len(same) > 1:
                for j in range(len(same)):
                    for k in range(j+1, len(same)):
                        same_list.append((same[j], same[k]))
    

    return len(mRet)
