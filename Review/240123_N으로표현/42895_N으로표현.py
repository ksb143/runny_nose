def solution(N, number):
    # dp[i]: i번째로 만들 수 있는 숫자의 집합
    dp = [set() for _ in range(9)]

    # 초기값 설정
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
    print(dp)

    # 다이나믹 프로그래밍
    for i in range(1, 9):
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(y - x)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)
                    if x != 0:
                        dp[i].add(y // x)

        # 목표 숫자가 생성되면 최솟값 반환
        if number in dp[i]:
            print(i)
            return i

    # 최솟값이 8보다 크면 -1 반환
    return -1


solution(5, 55)