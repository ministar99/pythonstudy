lst = [[0,0,0,0,0]
       ,[0,0,0,0,0]
       ,[0,0,0,0,0]
       ,[0,0,0,0,0]
       ,[0,0,0,0,0]]


i = 1
for x in range(0,5):
    for y in range(0,5):
        lst[x][y] = i
        i = i+1

for a in lst:
    print(a)
