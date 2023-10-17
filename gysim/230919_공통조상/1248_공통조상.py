def find_parent(idx):
    tmp = []
    while idx != 1:
        tmp.append(adj_c[idx])
        idx = adj_c[idx]
    return tmp


def find_c_anc():
    for i in range(len(PA)):
        for j in range(len(PB)):
            if PA[i] == PB[j]:
                return PA[i]


def find_subtree(idx):
    global cnt

    cnt += 1
    for i in range(2):
        if adj_p[idx][i]:
            find_subtree(adj_p[idx][i])


T = int(input())
for tc in range(1, T+1):
    # V : 정점의 개수, E : 간선의 개수, A,B : 공통조상 찾을 정점번호
    V, E, A, B = map(int, input().split())
    data = list(map(int, input().split()))
    # 인접행렬 만들기 -> 내 부모가 누군지 모름, 연결여부만 판단가능
    # 인접행렬 두개 만들기 -> 부모-자식, 자식-부모
    adj_p = [[0] * 2 for _ in range(V+1)]
    adj_c = [0] * (V+1)

    for i in range(0, E*2, 2):
        adj_c[data[i + 1]] = data[i]
        if not adj_p[data[i]][0]:
            adj_p[data[i]][0] = data[i+1]
        else:
            adj_p[data[i]][1] = data[i + 1]

    # [[0, 0], [2, 3], [4, 0], [5, 6], [7, 0], [9, 8], [11, 10], [12, 0], [0, 0], [0, 0], [0, 0], [13, 0], [0, 0], [0, 0]]
    # [0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 11]

    # 0행 부모, 1행 왼쪽자식, 2행 오른쪽자식 배열 만들기 -> 최대숫자 판단 못하겠음
    # 딕셔너리로 만들기
    # tree = {}
    # for i in range(0, E*2, 2):
    #     tree[data[i]] = []
    # for i in range(0, E*2, 2):
    #     tree[data[i]].append(data[i+1])

    # 부모 전부 찾아서 리스트에 넣기
    PA = find_parent(A)
    PB = find_parent(B)

    # 공통조상 찾기
    c_anc = find_c_anc()

    # 서브트리의 정점개수 찾기
    cnt = 0
    find_subtree(c_anc)

    print(f'#{tc} {c_anc} {cnt}')
