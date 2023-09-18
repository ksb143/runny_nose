N = int(input())
n = N
cnt = 0
if N % 5 == 0:
    cnt += N // 5
else:
    # 먼저 5로 나누기
    cnt += N // 5
    N = N % 5
    # 5 나누고 남은 것 3으로 나눠지면 나누기
    if N % 3 == 0:
        cnt += N // 3
    # 3으로 안 나눠지는 경우
    else:
        # cnt가 0보다 큰 경우 (5로 나눈 몫이 있을만큼 큰 값)
        if cnt > 0:
            while cnt > -1 and N != 0:
                N += 5
                cnt -= 1
                if N % 3 == 0:
                    cnt += N // 3
                    N = N % 3
        # cnt가 0인 경우 (5로 나눈 몫이 없을만큼 작은 값)
        else:
            while cnt > -1 and N != 0:
                if N % 3 == 0:
                    cnt += N // 3
                    N = N % 3
                else:
                    cnt -= 1

            
print(cnt)