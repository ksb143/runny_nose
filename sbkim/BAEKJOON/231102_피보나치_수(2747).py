n = int(input())

numbers = [0] * (n+1)
numbers[1] = 1

def fibo(idx, numbers):
    if idx == n+1:
        return
    numbers[idx] = numbers[idx-2]+numbers[idx-1]
    fibo(idx+1, numbers)


fibo(2, numbers)
10
print(numbers[n])