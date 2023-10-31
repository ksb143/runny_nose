# 1번부터 N 번의 도시들 사이에 길이 있거나 없다.
# 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 경로
# 한 번 갔던 도시로는 다시 갈 수 없다
# 가장 적은 비용을 들이는 경로
# 이동하는데 드는 비용은 행렬 W[i][j]로 주어진다
# W[i][j]와 W[j][i]는 다를 수 있다
# 모든 도시간의 비용은 양의 정수이다
# 비용이 0이면 연결되어있지 않다
import heapq


N = int(input())    # 도시의 수
W = [list(map(int, input().split())) for _ in range(N)]


def dijkstra(start):
    distance = [0xffffff] * N
    # visited = [0] * N
    pq = []
    heapq.heappush(pq, (W[start][start], start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for i in range(N):
            if W[now][i]:
                next_node = i
                cost = W[now][i]

                new_cost = dist + cost

                if distance[next_node] <= new_cost:
                    continue

                distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))
                # visited[i] = 1

    return max(distance), distance.index(max(distance))


result = []
for i in range(N):
    ans = 0
    ans1, idx1 = dijkstra(i)
    ans += ans1
    ans2, idx2 = dijkstra(idx1)
    ans += ans2
    result.append(ans)

# 다익스트라 두번 돌려서 더하기
print(min(result))
