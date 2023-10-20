# 답은 제대로 나오는데, 시간초과

from collections import deque

tc = int(input())   # 테스트 케이스 수
for _ in range(tc):
    n = int(input())    # 해빈이가 가진 의상 수

    # 의상 정보를 넣어줄 딕셔너리
    cloth_dict = {}
    # 의상 수만큼 순회하면서
    for i in range(n):
        # 의상이름, 의상종류 입력받음
        a, b = input().split()
        # 숫자를 키 값으로 의상종류를 value로 넣어줌
        cloth_dict[i] = b

    # 같은 종류의 의상을 입지 않으면서
    # 알몸이 아닌 상태로 의상을 입는 모든 경우의 수 개수
    total = 0
    # 비트마스킹으로 공집합을 제외한 부분집합 구현
    for i in range(1, 1 << n):
        # 의상 종류를 넣어줄 빈 배열
        clothes = deque()
        for j in range(n):
            if i & (1 << j):
                # 의상의 종류가 중복되면 이 부분집합 경우는 건너뛰기
                if cloth_dict[j] in clothes:
                    break
                else:   # 아니면
                    # 의상 종류를 clothes에 넣어주기
                    clothes.append(cloth_dict[j])
        # for문을 돌면서 break가 한번도 안 걸렸으면
        else:
            # 경우의 수 1 증가
            total += 1
    print(total)
