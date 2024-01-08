N = int(input())

x_list = [0] * N
y_list = [0] * N

for i in range(N):
    x, y = map(int, input().split())
    x_list[i] = x
    y_list[i] = y

x_len = max(x_list) - min(x_list)
y_len = max(y_list) - min(y_list)

print(x_len*y_len)