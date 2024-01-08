W, H, X, Y, P = map(int, input().split())

# 반지름 및 원의 중심 두개 구하기 
r = H // 2
cx1, cy1 = X, Y + r
cx2, cy2 = X + W, Y + r

# 사람 수
cnt = 0

for _ in range(P):
    x, y = map(int, input().split())
    # 사각형 내부일 때
    if X <= x <= X + W and Y <= y <= Y + H:
        cnt += 1
    # 원1 내부일 때
    elif X - r <= x < X:
        if r ** 2 >= (cx1 - x) ** 2 + (cy1 - y) ** 2:
            cnt += 1
    # 원2 내부일 때
    elif X + W < x <= X + W + r:
        if r ** 2 >= (cx2 - x) ** 2 + (cy2 - y) ** 2:
            cnt += 1
print(cnt)