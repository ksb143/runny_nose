di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(i, j):
    queue = [(i, j)]
    apartments[i][j] = 0
    cnt = 1

    while queue:
        r, c = queue.pop(0)
        for i in range(4):
            nr, nc = r + di[i], c + dj[i]
            if 0 <= nr < N and 0 <= nc < N and apartments[nr][nc] == 1:
                queue.append((nr, nc))
                apartments[nr][nc] = 0
                cnt += 1
                
    return cnt


N = int(input())

apartments = [[] for _ in range(N)]
for i in range(N):
    apartments[i] = list(map(int, input()))

cnt = 0     # 단지를 세는 변수
complex_num = []        # 단지 내 집의 수를 넣는 리스트

for i in range(N):
    for j in range(N):
        if apartments[i][j] == 1:
            complex_num.append(bfs(i, j))
            cnt += 1

complex_num.sort()      # 오름차순

print(cnt)

for num in complex_num:
    print(num)
