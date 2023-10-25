N = int(input())

# 다각형의 대각선의 교점 = 전체 N개의 점에서 4개의 점 고르기
result = N * (N - 1) * (N - 2) * (N - 3) // 24
print(result)