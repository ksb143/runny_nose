N = input()
F = int(input())

length = len(N)

# 해당 숫자에서 10의 자리를 빼기
num = N[:length-2]
num = int(num) * 100

# 나눠지는 숫자가 나오면 바로 종료
for n in range(100):
    if (num + n) % F == 0:
        ans = n
        break
# 해당 숫자 맞는 형식으로 바꿔서 출력
print('{0:02d}'.format(ans))