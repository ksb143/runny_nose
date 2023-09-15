dir_idx = {
    1: [-1, 0], # 상
    2: [0, 1],  # 우
    3: [1, 0],  # 하
    4: [0, -1]  # 좌
}
T = int(input())
for tc in range(1,1+T):
    xa,ya =1,1
    xb,yb =10,10
    # <<<<  모든 사용자가 1)'충전한 양'의 2)'합'의 3)'최댓값'을 구하라. >>>>
    l = list(map(int,input().split()))
    M,A = l[0],l[1] # M= 인간의 총 이동시간: 20, A= 배터리충전기의 갯수: 3
    A_move = list(map(int,input().split())) # A의 이동 경로, 총 M개
    B_move = list(map(int,input().split())) # B의 이동 경로, 총 M개
    print(A_move,B_move)
    for i in range(M):
        A_move[i]
        B_move[i]
    for a in range(A):
        ll = list(map(int,input().split()))
        [x,y], cover, capa = [ ll[0],ll[1] ],ll[2],ll[3]
        # print([x, y], cover, capa)
        BC_range = [[x,y]]
        for k in range(cover):
            for i in range(1,4+1):
                list(x+dir_idx[i][0], y+dir_idx[i][1])
        print(a+1,BC_range)
