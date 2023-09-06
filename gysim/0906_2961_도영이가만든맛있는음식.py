def solve(idx):
    global min_v
    
    if idx == N:
        sour = 1
        bitter = 0
        cnt = 0
        for i in range(N):
            if used[i]:
                sour *= ingredient[i][0]
                bitter += ingredient[i][1]
            else:
                cnt += 1
            
        if cnt != N and abs(sour-bitter) < min_v:
            min_v = abs(sour-bitter)
        
        return

    used[idx] = 1
    solve(idx+1)
    used[idx] = 0
    solve(idx+1)


N = int(input())    # N개의 재료
# 각 재료의 신맛 S, 쓴맛 B
ingredient = [list(map(int, input().split())) for _ in range(N)]

min_v = 0xffffffff

used =[0] * N

solve(0)

print(min_v)

# 신맛의 곱, 쓴맛은 합이다
# 신맛과 쓴맛의 차이 최소값 출력
# 재료는 적어도 하나 사용해야한다

# 1. 공집합을 제외한 모든 부분집합 만들기
# 2. 반복문 돌리기