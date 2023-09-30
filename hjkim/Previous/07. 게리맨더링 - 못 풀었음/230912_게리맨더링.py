# powerset : idx번째에 들어갈 원소를 고름
def powerset(idx, N):
    if idx == N:
        return group_a, group_b
    if idx == N:
        group_a.clear()
        group_b.clear()
    if bit[i]:
        group_a.append(idx)
    else:
        group_b.append(idx)
    bit[idx] = 1
    powerset(idx+1, N)
    bit[idx] = 0
    powerset(idx+1, N)


N = int(input())
people = list(input().split())
data = [list(map(int, input().split())) for _ in range(N)]
adj = [[0]*(N+1) for _ in range(N+1)]
bit = [0] * (N)
group_a = []
group_b = []


# 그래프 인접행렬로 나타내기
for i in range(N):
    for j in range(data[i][0]):
        adj[i + 1][data[i][j + 1]] = 1
        adj[data[i][j + 1]][i + 1] = 1

# data를 돌면서 부분집합 만드는 함수 구현하기
powerset(1, N)
print(group_a,end=' ')
print(group_b)
