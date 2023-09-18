N = int(input())
balloons = list(map(int, input().split()))

# 첫 번째 풍선 빼기
idx = 0
# 풍선에 든 종이 꺼내기
paper = balloons[idx]
# 꺼낸 풍선 초기화
balloons[idx] = 0
# 풍선에 든 종이 프린트
print(idx+1, end=' ')
# 풍선 셀 변수
cnt = 1

# 풍선 종이 총 개수보다 적을 때까지 하기
while cnt < N:
    # idx 재정의
    idx = idx + paper
    # 초기화된 풍선이 아닐 경우
    if balloons[idx % N] != 0:
        paper = balloons[idx % N]
        balloons[idx % N] = 0
        if idx % N >= 0:
            print((idx % N) + 1, end=' ')
        else:
            print(abs(idx % N), end=' ')
        cnt += 1
    # 초기화된 풍선일 경우
    else:
        while balloons[idx % N] == 0:
            if idx > 0:
                idx += 1
            else:
                idx -= 1
        paper = balloons[idx % N]
        balloons[idx % N] = 0
        if idx % N >= 0:
            print((idx % N) + 1, end=' ')
        else:
            print(abs(idx % N), end=' ')
        cnt += 1
