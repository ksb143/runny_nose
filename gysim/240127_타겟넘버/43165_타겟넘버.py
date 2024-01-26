def dfs(idx, result, numbers, target):

    if idx == len(numbers):
        if result == target:
            return 1
        return 0

    plus = dfs(idx + 1, result + numbers[idx], numbers, target)
    minus = dfs(idx + 1, result - numbers[idx], numbers, target)
    return plus + minus


def solution(numbers, target):

    answer = dfs(0, 0, numbers, target)

    # print(answer)
    return answer


solution([4, 1, 2, 1], 4)
