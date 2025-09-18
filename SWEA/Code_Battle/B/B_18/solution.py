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
    

    dq_set_list = list(set(dq_list))
    count_dict = Counter(dq_list)
    same_len_dict = defaultdict(list)

    for word in dq_set_list:
        same_len_dict[len(word)].append(word)

    index_dict = {w: idx for idx, w in enumerate(dq_set_list)}
    graph = [[] for _ in range(len(dq_set_list))]

    for words in same_len_dict.values():
        same_dict = defaultdict(list)
        for w in words:
            for pos in range(len(w)):
                temp = w[:pos] + '*' + w[pos+1:]
                same_dict[temp].append(w)
        for mask, same_words in same_dict.items():
            if len(same_words) > 1:
                for i in range(len(same_words)):
                    for j in range(i+1, len(same_words)):
                        a, b = same_words[i], same_words[j]
                        graph[index_dict[a]].append(index_dict[b])
                        graph[index_dict[b]].append(index_dict[a])

    # 2. BFS로 그룹 찾기
    visited = [False] * len(dq_set_list)
    groups_info = []  # (대표어, 그룹총전달수)

    for i in range(len(dq_set_list)):
        if not visited[i]:
            q = deque([i])
            visited[i] = True
            group_words = []
            while q:
                cur = q.popleft()
                group_words.append(dq_set_list[cur])
                for nxt in graph[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)
            # 대표어 선정 (전체 기준 count_dict 사용)
            max_freq = max(count_dict[w] for w in group_words)
            candidates = [w for w in group_words if count_dict[w] == max_freq]
            rep_word = min(candidates)  # 동률이면 사전순
            # 그룹 총 전달 횟수 (전체 기준)
            group_total = sum(count_dict[w] for w in group_words)
            groups_info.append((rep_word, group_total))

    # 3. 인기 검색어 정렬 (전달수 내림차순 → 대표어 사전순)
    groups_info.sort(key=lambda x: (-x[1], x[0]))

    # 4. 상위 5개 대표어 출력
    top_5 = [rep for rep, _ in groups_info[:5]]
    mRet = top_5

    return len(mRet)
