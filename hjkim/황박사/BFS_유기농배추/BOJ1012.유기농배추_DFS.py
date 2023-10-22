def dfs(row, col):
    stack = [(row, col)]

    while stack:
        row, col = stack.pop()
        visited[row][col] = 1

        # Define the possible moves (up, down, left, right)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < N and 0 <= new_col < M and my_map[new_row][new_col] == 1 and not visited[new_row][
                new_col]:
                stack.append((new_row, new_col))


T = int(input())
for tc in range(1, T + 1):
    M, N, K = map(int, input().split())
    my_map = [[0] * M for _ in range(N)]
    dots = [list(map(int, input().split())) for _ in range(K)]

    for idx in range(K):
        col, row = dots[idx][0], dots[idx][1]
        my_map[row][col] = 1

    visited = [[0] * M for _ in range(N)]
    answer = 0

    for row in range(N):
        for col in range(M):
            if my_map[row][col] == 1 and not visited[row][col]:
                visited[row][col] = 1
                dfs(row, col)
                answer += 1

    print(answer)
