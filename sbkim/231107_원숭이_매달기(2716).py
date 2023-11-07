from collections import deque

N = int(input())

for _ in range(N):
    vines = deque((input()))
    monkey = 0
    # 덩굴이 있는 경우
    if vines:
        # 깊이를 재는 변수
        max_depth = 0
        # 덩굴의 개수를 실시간으로 반영하는 변수
        cnt = 0
        for v in vines:
            # 왼덩일 경우
            if v == '[':
                cnt += 1
                # 최대 깊이 갱신
                if max_depth < cnt:
                    max_depth = cnt
            # 오덩일 경우
            else:
                cnt -= 1
        monkey = 2 ** max_depth
    # 덩굴이 없는 경우
    else:
        monkey = 1

    print(monkey)


