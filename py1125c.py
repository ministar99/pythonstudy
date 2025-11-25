number1 = int(input('첫번째 정수 :'))
number2 = int(input('두번째 정수 :'))
a= 0
for i in range(min(number1, number2),0, -1):
    if number1 % i == 0 and number2 % i == 0:
        a = i
        break
b = 0
for j in range(max(number1, number2), (number1*number2)+1):
    if j % number1 == 0 and j % number2 == 0:
        b = j
        break

print(f"최대공약수 : {a}")
print(f"최소공배수 : {b}")