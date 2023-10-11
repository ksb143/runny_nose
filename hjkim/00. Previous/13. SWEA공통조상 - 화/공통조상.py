T = int(input())
for tc in range(1, T+1):
    V, E, S, G = map(int, input().split())
    edges = list(map(int, input().split()))
    parents = [edges[i] for i in range(0, 2*E, 2)]
    child = [edges[i+1] for i in range(0, 2*E, 2)]
