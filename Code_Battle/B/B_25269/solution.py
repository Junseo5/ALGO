# 25269. [Pro] 온라인마트 Python
#####solution.py

# 딕셔너리 구조
# [Category 1 -> [Company 1 -> {ID : Price}]]

class RESULT:
    def __init__(self, cnt, IDs):
        self.cnt = cnt
        self.IDs = IDs  # [int] * 5


def init() -> None:
    global sell_dict, id_pointer_dict
    # 카테고리 리스트 안에 컴퍼니 리스트 안에 딕셔너리 추가 항상-1해줘야함
    sell_dict = [[{} for i in range(5)] for j in range(5)]
    id_pointer_dict = {}


def sell(mID, mCategory, mCompany, mPrice):
    # 카테고리 컴퍼니 가격 id 상품 판매 시작
    # 셀 딕셔너리에 추가
    # 카테고리 컴퍼니 같은 이미 판매중인 상품 개수 반환
    # 해당 딕셔너리 len 찍어서 리턴

    sell_dict[mCategory - 1][mCompany - 1][mID] = mPrice
    id_pointer_dict[mID] = (mCategory - 1, mCompany - 1)

    sell_cnt_len = len(sell_dict[mCategory - 1][mCompany - 1])

    return sell_cnt_len


def closeSale(mID):
    # 카테고리 컴퍼니 id_pointer_dict에 저장되어 있는 좌표에 값 수정

    if id_pointer_dict.get(mID) == None:
        return -1

    temp_mCategory, temp_mCompany = id_pointer_dict[mID]

    result = sell_dict[temp_mCategory][temp_mCompany][mID]

    del sell_dict[temp_mCategory][temp_mCompany][mID]
    del id_pointer_dict[mID]

    return result


def discount(mCategory, mCompany, mAmount):
    # 메인 딕셔너리 모든 상품 가격을 mAmount만큼 낮춤
    # 만약 낮춘 가격이 0 이하면 del 및 id 추출하여 id_pointer_dict 값 제거
    # 낮춘 후 카테고리, 컴퍼니 같은 품목 판매되는 개수 반환

    # 순회 중 0보다 작아진 삭제될 아이디 저장 리스트
    del_id = []

    for i_key, i_value in sell_dict[mCategory - 1][mCompany - 1].items():
        price = i_value - mAmount
        sell_dict[mCategory - 1][mCompany - 1][i_key] = price

        if price <= 0:
            del_id.append(i_key)

    for i in del_id:
        closeSale(i)

    sell_cnt_len = len(sell_dict[mCategory - 1][mCompany - 1])

    return sell_cnt_len


def show(mHow, mCode):
    # 조건 mHow = 0 이면 모든 상품
    # 조건 mHow = 1 이면 카테고리가 mCode인 상품들
    # 조건 mHow = 2 이면 컴퍼니가 mCode인 상품들

    # mHow 조건에 따라 가격이 낮은 순으로 최대 5개의 상품 아이디를 반환
    # 가격이 같으면 id가 더 낮은 값을 우선 반환

    # sort시 시간초과 가능성
    # 딕셔너리 key value 그대로 넘긴 후 value만 min값 비교 후 5개 추가
    # 튜플형식 앞에 value 뒤에 key 넣고 5번 순회 끝

    def min_sort(sample_dict):
        min_list = [(100000000, None)] * 5

        for i_key, i_value in sample_dict.items():
            if i_value > min_list[-1][0]:
                continue
            for j in range(5):
                # 들어온 값 5 기존값 1 7 inf inf inf 면 쉬프트 해당값 j+1부터 4번 인덱스까지를 j부터 3번인덱스로 변경
                if i_value < min_list[j][0]:
                    min_list[j + 1:] = min_list[j:4]
                    min_list[j] = (i_value, i_key)
                    break
                elif i_value == min_list[j][0]:
                    if i_key < min_list[j][1]:
                        min_list[j + 1:] = min_list[j:4]
                        min_list[j] = (i_value, i_key)
                        break

        result_min_list = []
        cnt = 0
        for i in min_list:
            if i[1] == None:
                break
            result_min_list.append(i[1])
            cnt += 1

        return cnt, result_min_list

    result_list = []
    result_cnt = 0
    temp_dict = {}

    if mHow == 0:
        for i in sell_dict:  # 카테고리
            for j in i:  # 컴퍼니
                temp_dict.update(j)

        result_cnt, result_list = min_sort(temp_dict)
    elif mHow == 1:
        for i in sell_dict[mCode - 1]:  # 컴퍼니
            temp_dict.update(i)

        result_cnt, result_list = min_sort(temp_dict)
    elif mHow == 2:
        for i in range(5):  # 카테고리
            temp_dict.update(sell_dict[i][mCode - 1])

        result_cnt, result_list = min_sort(temp_dict)

    return RESULT(result_cnt, result_list)