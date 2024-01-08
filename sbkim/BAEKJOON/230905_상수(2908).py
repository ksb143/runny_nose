num1, num2 = input().split()

num1 = int(''.join(reversed(num1)))
num2 = int(''.join(reversed(num2)))

if num1 > num2:
    print(num1)
else:
    print(num2)