# 머잠


S = int(input("숫자를 입력하시오 :"))
s = (2*S + 1)

lst = [[0]*s for _ in range(s)]

i = len(lst)-1
j = len(lst[i])//2

for N in range(1,s*s+1):
    lst[i][j] = N

    next_i = i + 1
    next_j = j - 1

    if next_i >= len(lst):
        next_i = 0
    if next_j < 0:
        next_j = len(lst[0])-1
    if lst[next_i][next_j] != 0:
        next_i = i + 1
        next_j = j

    i = next_i
    j = next_j

    for row in lst:
      print(row)