# 시간초과
from collections import deque

tc = int(input())   # 테스트 케이스 수
for _ in range(tc):
    n = int(input())    # 해빈이가 가진 의상 수

    cloth_dict = {}
    for i in range(n):
        a, b = input().split()
        cloth_dict[i] = b

    total = 0
    for i in range(1, 1 << n):
        clothes = deque()
        for j in range(n):
            if i & (1 << j):
                # 의상의 종류가 중복되면 개수 빼기
                if cloth_dict[j] in clothes:
                    break
                else:
                    clothes.append(cloth_dict[j])
        else:
            total += 1
    print(total)
