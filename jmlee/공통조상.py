from collections import deque
def findP1(n): #첫번째 주어진 정점의 조상찾기
    if P[n]:  # 조상들을 찾는 딕셔너리에 값이 있을때
        P1.append(P[n][0]) #조상을 P1에 담고
        findP1(P[n][0]) #재귀를 이용해 한단계 위 조상을 값으로 넣어 다음 조상찾기
def findP2(n): #위에꺼와 동일 다시
    if P[n]:
        P2.append(P[n][0])
        if P[n] in P1:
            return
        findP2(P[n][0])
def findcnt(n): #공통조상을 입력받아 트리 순회하기
    global cnt #카운트 글로벌로 받고
    for i in data[n]: # 해당 조상의 자손들을 딕셔너리를 통해 받아오기
        cnt+=1 #자손이 하나있을때마다 카운트+1
        findcnt(i) #재귀를 통해 그 밑의 자손으로 넘어가서 그 자손의 자손 있나 찾아보기
T=int(input())
for tc in range(1,T+1):
    V, E, T1, T2= map(int,input().split())
    temp=list(map(int,input().split()))
    data = {i: [] for i in range(V+1)} # 노드의 구조를 딕셔너리 형태로 받기(받기 데이터 최소화)
    P={i: [] for i in range(V+1)} # 각 노드의 부모역시 딕셔너리 형태로 저장
    for i in range(0,len(temp),2): #받은 입력값을 2칸씩보기
        data[temp[i]].append(temp[i+1]) #1-2를예를들면 1의 기준 2가 자손
        P[temp[i+1]].append(temp[i])   # 2기준 1이 부모
    P1=deque() #첫번째 주어진 정점의 조상들 담을 데큐만들기
    P2=deque() #두번째 주어진 정점의 조상들 담을 데큐만들기
    findP1(T1) #위 함수에서 설명함
    findP2(T2)
    # 두 조상 함수를 찾았으면 이제 본격적으로 공통 조상 찾기
    if len(P2)<=len(P1): #사실 이조건문은 별 의미없음
        a= P1.popleft()  # 한쪽에서 왼쪽부터 계속 뽑아서(왼쪾부터 하는 이유 여러 공통조상중에 가장 하위 조상을 찾기위해)
        while not a in P2: # 다른쪽 조상리스트에 있을때까지 뽑기
            a = P1.popleft() #다른쪽에도 있으면 공통조상
    else:
        a = P2.popleft()
        while not a in P1:
            a = P2.popleft()
    #위 과정을 거쳐 공통 조상을 찾았으니 이제 공통조상의 하위 갯수 찾기
    cnt=1 #숫자 셀 카운트(자기자신(공통조상)포함이라 1부터시작)
    findcnt(a)#다시 위 함수 설명으로 가시오
    #이제 공통조상과 그 조상의 자식수를 다 셌으니 입력값 출력
    print(f'#{tc} {a} {cnt}')