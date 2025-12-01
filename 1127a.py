def allsum (N):
    if N == 1:
        return 1
    else:
        return N+allsum(N-1)

total=allsum(100)
print(total)