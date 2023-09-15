# X 상 우 하 좌
delta = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]

T = int(input())
for tc in range(1, T+1):
    # M : 총 이동시간, A : BC의 개수
    M, A = map(int, input().split())
    # 각 사용자 별 이동 정보, M개의 숫자, 숫자는 이동방향 의미
    data_A = list(map(int, input().split()))
    data_B = list(map(int, input().split()))
    # A줄에 걸쳐 좌표 X, Y, 충전범위 C, 처리량 P
    BC = [list(map(int, input().split())) for _ in range(A)]

    # 좌표는 (1, 1) ~ (10, 10)
    maps = [[0] * 11 for _ in range(11)]
    checked = [[0] * 11 for _ in range(11)]

    # 두 지점 사이의 거리 D >= abs(x1-x2) + abs(y1-y2) 이면 접속 가능
    # 1. bc좌표에서 영역만큼 계산해서 1씩 더해줌, 겹치는 부분은 1 이상으로 판단
    for i in range(A):
        r, c = BC[i][0], BC[i][1]
        for j in range(1, 11):
            for k in range(1, 11):
                if abs(r-j) + abs(c-k) <= BC[i][2]:
                    checked[j][k] += 1
                    maps[j][k] += BC[i][3]

    # 사용자A는  (1,1)에서, 사용자 B는 (10,10)에서 출발
    ar, ac = 0, 0
    br, bc = 10, 10

def charge(r, c):
    total = 0
    if checked[r][c] == 1:
        total += maps[r][c]
    elif checked[r][c] > 1:


    for i in range(M):
        d = data_A[i]



    # 두 지역이 겹치면 두개 중 하나를 선택하여 접속
    # 한 bc에 두명의 사용자가 접속한 경우, 접속한 사용자의 수만큼 충전양을 분배


