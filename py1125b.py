def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

p= []
for num in range(2, 10000):
    if is_prime(num):
        p.append(num)
        print(num, end=' ')