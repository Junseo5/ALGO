# 6319. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 1

def palindrome(n):
    a = []
    for i in range(len(n)-1, -1, -1):
        a.append(n[i])
        
    sum = ''.join(a)
    
    print(sum)

    if n == sum:
        print("입력하신 단어는 회문(Palindrome)입니다.")

palindrome(input())