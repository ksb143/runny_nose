
def DFS(x, y, setset, cnt):
    global max_num
    if max_num < cnt:
        max_num = cnt
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        # if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and word[nx][ny] not in setset:
        if 0 <= nx < R and 0 <= ny < C and word[nx][ny] not in setset:
            # visited[nx][ny] = 1
            # setset.add(word[nx][ny])
            DFS(nx, ny, setset+word[nx][ny], cnt+1)
            # setset.remove(word[nx][ny])
            # visited[nx][ny] = 0

R, C = map(int, input().split())
# 세로 R칸, 가로 C칸
word = [list(input()) for _ in range(R)]
# input 받은 글자 목록
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# 이동해야하니까!
# 시작점은 (0,0)임
# alphabet = {word[0][0]}
alphabet = word[0][0]
# 안에 있다 없다를 판단하려면 set()을 쓰거나
# 배열의 인덱스로 체크하는 것이 좋다!
# visited = [[0]*C for _ in range(R)]
max_num = 0
DFS(0, 0, alphabet, 1)
print(max_num)
