# 25288 . 라인도시건설

# n 토지 길이는 최대 1억
# 빌딩 길이는 최대 n까지

# 건설 및 제거 시 건물 공간의 시작지점과 끝지점 좌표 저장
# 기존 관리중이던 space 공간을 들어온 건물의 길이만큼 제거 후 추가, 수정
# 제거 시 하나하나 찾는 시간이 오래걸리기에 들어온 주소값으로 밸류값 계산 후
# 제거된 space 좌표 저장소에 오리지널 space 좌표 저장소에 들어있는 값과 같은 값을 저장
# 건설 시 제거된 좌표와 같은 값이 있으면 해당 값은 무시 후
# 다음 제거된 좌표에 없는 가장 큰 space 좌표 값에 중앙에 빌딩 건설

#####solution.py
def init(N: int) -> None:
    pass

def build(mLength: int) -> int:
    return -1

def demolish(mAddr: int) -> int:
    return -1