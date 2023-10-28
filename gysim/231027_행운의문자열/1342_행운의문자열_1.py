S = input()     # 알파벳 소문자로만 이루어진 문자열, 최대 길이는 10
N = len(S)      # 문자열의 길이
visited = [0] * N   # i번째 문자를 사용했는지 확인할 배열
result = set()  # 서로 다른 문자열 -> 중복 제거 위해 빈 세트 만들기


# 인접해 있는 모든 문자가 같지 않은 문자열을 행운의 문자열이라고 한다
# 문자열 S에 나오는 문자를 재배치했을 때 서로 다른 행운의 문자열이 몇 개인지 출력

# cnt : 뽑은 문자의 개수, word : cnt 개만큼 고른 문자열
def comb(cnt, word):
    # 행운의 문자열인지 검사
    # 2글자 이상이고 (cnt-1)번째 문자와 왼쪽 문자가 다른지 비교
    # (cnt-1)인 이유는 인덱스라서 -1 해줌
    if len(word) > 1 and word[cnt-1] == word[cnt-2]:
        # 행운의 문자열 조건을 만족하지 않으면 돌아가기
        return
    
    # N개만큼 문자를 뽑았으면
    if cnt == N:
        # 중복 있는지 확인하고 (이건 꼭 필요한건 아님)
        if word not in result:
            # result에 재배치한 문자열을 넣어줌
            result.add(word)
        return
    
    # N만큼 순회하면서
    for i in range(N):
        # i번째 문자를 안썼으면
        if not visited[i]:
            # 썼다고 표시
            visited[i] = 1
            # 다음 문자열 뽑으러 가기
            comb(cnt+1, word + S[i])
            # 다 썼음
            visited[i] = 0

# 함수 실행
comb(0, '')

# 서로 다른 행운의 문자열 개수 출력
print(len(result))


# 참고 ############################################
# from itertools import permutations

# S = input()
# N = len(S)
# result = set()

# for permuted in set(permutations(S, N)):
#     is_lucky = all(permuted[i] != permuted[i + 1] for i in range(N - 1))
#     if is_lucky:
#         result.add(permuted)

# print(len(result))
