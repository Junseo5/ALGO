# 1936. 1대1 가위바위보

# 가위1 바위2 보3

a, b = map(int, input().split())

if (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
    print("A")
elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    print("B")