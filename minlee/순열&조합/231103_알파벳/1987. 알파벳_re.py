def DFS(x, y, setset, cnt):
    global max_num
    if max_num < cnt:
        max_num = cnt
        # 최대 값보다 이동한 거리가 더 크면 그 쪽으로 간다
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        # 새로운 위치 가준다
        if 0 <= nx < R and 0 <= ny < C and word[nx][ny] not in setset:
            DFS(nx, ny, setset+word[nx][ny], cnt+1)
            # 새로운 위치로, 문자를 넣어서, 카운트를 올린다!

R, C = map(int, input().split())
# 세로 R칸, 가로 C칸
word = [list(input()) for _ in range(R)]
# input 받은 글자 목록
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# 이동해야하니까!
# 시작점은 (0,0)임
alphabet = word[0][0]
# 처음 값을 넣어준다(시작점이니까!)
max_num = 0
# 최대 이동거리 찾으려고!
DFS(0, 0, alphabet, 1)
print(max_num)