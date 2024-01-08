N = int(input())

build = []

for _ in range(N):
    h, w = map(int, input().split())
    build.append((h, w))

order = []

for hi, wi in build:
    # 덩치 등수는 k + 1 이므로 기본으로 1을 줌
    k = 1
    for hj, wj in build:
        # 나보다 덩치가 크면 1 더하기
        if hi < hj and wi < wj:
            k += 1
    order.append(k)

print(*order)
