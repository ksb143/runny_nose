def tail_to_head(data0,N,idx): # data: 원래정보, N: 회전 목표횟수
    global result
    if idx == N-1: # 0 == 4
        # print('A',idx,data0)
        result.append(data0)
        return
    else:
        # print('B',idx,data0)
        result.append(data0)
        data1 = data0[-1] + data0[:-1]
        tail_to_head(data1,N,idx+1)
T= int(input())
for tc in range(1,1+T):
    N,K = map(int,input().split()) # 20 14
    n = N//4 # 5
    data = input()
    # print(N,K,n,data)
    # print()
    result = []
    data0 = data[:]
    tail_to_head(data0,n,0)
    final = []
    # print(result)
    for i in range(n): # 0 1 2 3 4
        for j in range(0,N,n):
            final.append(int(result[i][j:j+n],16))
    # print(final)
    final = list(set(final))
    final.sort(reverse=True)
    print(f'#{tc} {final[K-1]}')