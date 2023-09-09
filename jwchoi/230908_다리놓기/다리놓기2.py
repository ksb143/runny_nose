#### 모르는사람 코드
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(int(factorial(M) / (factorial(N) * factorial(M - N))))


#### 수빈 코드

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    # 팩토리얼을 넣을 리스트 만들기
    mp = [0] * (M+1)
    mp[0] = 1
    np = [0] * (N+1)
    np[0] = 1
    rp = [0] * (M-N+1)
    rp[0] = 1
    # 팩토리얼을 dp로 구현
    for i in range(1, M+1):
        mp[i] = mp[i-1]*i
        if i <= (N):
            np[i] = np[i-1]*i
        if i <= (M-N):
            rp[i] = rp[i-1]*i
    # float 형으로 나와서 int형으로 교체 (왜 그런지는 모르겠음)
    ans = int(mp[-1]/(np[-1]*rp[-1]))
    print(ans)

#### 모르는사람 코드

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())

    result = 1
    for i in range(n):
        result *= m
        m -= 1
    devisior =1
    for i in range(2,n+1):
        devisior  *= i
    print(result // devisior)