# 2050. 알파벳을 숫자로 변환

n = input()

n_list = []

for i in n:
    n_list.append(str(ord(i) - ord('A') + 1))

print(' '.join(n_list))

# ord() 함수 아스키코드 10진수로 변환해준다. ex) 'A'를 65로 반환