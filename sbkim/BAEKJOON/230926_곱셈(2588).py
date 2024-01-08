A = int(input())
B = input()
result = 0
for i in range(2, -1, -1):
    print(A*int(B[i]))
    result += A*int(B[i])*(10**(2-i))
print(result)
