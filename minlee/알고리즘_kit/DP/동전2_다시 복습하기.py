n, k = map(int,input().split())
given = set()
for _ in range(n):
    given.add(int(input()))
given = list(given)
given.sort()
# 위에 과정은 가지고 있는 동전의 중복을 없애고 오름차순으로 정리
n = len(given) #중복을 제거하는 과정에서 길이가 바뀔수도 있으므로 인덱스 에러 방지 위해 재지정
dp = [-1] * (k + 1) # 값 채워나갈 리스트 작성
pointer = 0 #아직 안쓰인 더 큰 값의 동전들의 최소 값의 인덱스
check = float("INF") # 밑에 최소값이 바꼈나(가진 동전으로 만들 수 있는 금액인가) 체크 하는 용
for i in range(1, k + 1): #1에서부터 목표인 k까지 채워나갈 반복문
    if pointer < n and i == given[pointer]:
    #앞의 부분은 인덱스에러방지 뒷부분은 해당 동전과 줘야할 동전의 값이 같으면 그 동전 하나 주는게 최소 방법이므로 1로 기록하고 넘어가기
        dp[i] = 1
        pointer += 1 #안쓰인 동전중 최소 값이 쓰였으니 다음 최소값을 가르키기위해 인덱스 1증가
        continue
    min_num = float("INF") #확인할 최소값
    for j in range(0, pointer): # 쓰인 동전들까지만 반복문이 돌게 설정
        if dp[i - given[j]] != -1:
            #줘야할 돈에서 가지고 있는 동전의 가치를 뺀 곳의 거스름돈 가짓수 기록이 있으면
            #거기서 해당 동전값만큼 한번 더 주면 i의 값을 만들 수 있으니 +1
            if dp[i - given[j]] + 1 < min_num:
                min_num = dp[i - given[j]] + 1
            #근데 가진 동전이 3,5 이고 목표 동전이 15면 12에서 3주는 법과 10에서 5주는 법이 있으니
            #각 경우에 값을 다 비교해서 최소 가짓수의 값만 기록
    if check != min_num: # min_num이 바꼈다는 건 위의 과정에서 만들 수 있는 금액이니까
        dp[i] = min_num #구한 최소 가짓수 기록
