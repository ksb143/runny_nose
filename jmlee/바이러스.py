# 2606. 바이러스

computer = int(input())     # 컴퓨터 갯수
couple = int(input())       # 간선 갯수
# 네트워크 정보 담기
adj = [[] for _ in range(computer+1)]
for _ in range(couple):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

# 방문 표시
visited = [0]*(computer+1)

ans = 0         # 바이러스에 걸리는 컴퓨터 갯수 변수
infect = [1]    # start : 1번 컴퓨터 바이러스  

while infect:
    step = infect.pop(0)
    if visited[step] == 0:
        visited[step] = 1
        ans += 1
        for i in adj[step]:
            infect.append(i)

print(ans-1)
