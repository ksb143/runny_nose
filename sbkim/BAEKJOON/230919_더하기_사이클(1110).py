N = input()
if len(N) == 1:
    N = '0' + N
cnt = 0

new_number = N[1] + str((int(N[0]) + int(N[1])) % 10)
cnt += 1

while new_number != N:
    new_number = new_number[1] + str((int(new_number[0]) + int(new_number[1])) % 10)
    cnt += 1
print(cnt)