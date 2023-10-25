def combination_count(n, k):
    # n개 중에 k개를 조합 으로 뽑는 것이 불 가능한 경우
    if n < 0 or k < 0 or k > n:
        return 0
    # n개 중에 k개를 조합 으로 뽑는 것이 가능한 경우
    # 이항 계수를 계산 후, 조합의 수를 반환
    result = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        result *= (n - i)
        result //= (i + 1)

    return result

# 예제 사용
n = int(input())
print(combination_count(n,4))