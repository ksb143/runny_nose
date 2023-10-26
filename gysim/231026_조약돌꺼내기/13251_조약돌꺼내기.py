# 조약돌의 색상은 1부터 M 사이의 수
M = int(input())

# 각 색상의 조약돌이 몇 개 있는지 주어진다
# 조약돌 개수는 1부터 50 사이의 자연수
N = list(map(int, input().split()))

# 뽑을 조약돌의 개수
K = int(input())

ans = 0

# 주어진 조약돌 색상만큼 순회
for i in range(M):
    tmp = 1     # 확률 초기값, 곱하기라서 1로 초기화
    color = N[i]    # 현재 색상의 조약돌 개수
    total = sum(N)  # 조약돌의 총 개수
    # 뽑을 조약돌의 개수만큼 반복
    for j in range(K):
        # 같은 색상을 뽑을 확률 = 해당 색상의 수 / 전체 수
        tmp *= color / total
        # 하나를 뽑고 남은 것 중에서 뽑을 확률 = (해당 색상의 수 - 1) / (전체 수 - 1)
        # 그 다음은 또 한 개씩 빼주고 확률 구하기
        color -= 1
        total -= 1
    # 한 색상 당 조약돌을 K 개만큼 뽑은 확률 더해주기
    ans += tmp

# 뽑은 조약돌이 모두 같은 색일 확률 출력
print(ans)
