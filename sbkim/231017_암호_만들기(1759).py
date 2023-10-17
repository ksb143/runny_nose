def comb(idx, cnt, C, L, check):
    # 종료 조건
    if idx == C:
        # L개 뽑지 않았을 때 경우 넘기기
        if cnt != L:
            return
        # L개 뽑았을 경우
        # 빈 문자열 만들기
        word = ''
        # 해당 순서 문자열 빈 문자열에 넣기
        for i in range(C):
            if check[i]:
                word += alpha[i]
        # 만든 results 리스트에 넣기
        results.append(word)
        return

    # 알파벳 해당 idx에서 뽑은 경우 체크 표시
    check[idx] = 1
    # 다음 idx로 가는데 뽑았으니 cnt += 1 하기
    comb(idx+1, cnt+1, C, L, check)
    # 알파벳 해당 idx에서 안 뽑은 경우 체크 다시 되돌려주기
    check[idx] = 0
    # 다음 idx로 가는데 안 뽑았으니 cnt는 그대로
    comb(idx+1, cnt, C, L, check)


L, C = map(int, input().split())
alpha = input().split()

# 정렬하는 버릇 있다했으니 오름차순으로 정렬해주기
alpha.sort()

check = [0] * C

results = []

comb(0, 0, C, L, check)

# 실제 정답에 해당하는 리스트
ans = []

for result in results:
    # 모음, 자음을 세는 것
    vow, con = 0, 0
    for i in result:
        # 모음인 경우
        if i in ['a', 'e', 'o', 'u', 'i']:
            vow += 1
        # 자음인 경우
        else:
            con += 1
    # 모음 1개 이상, 자음 1개 이상인 경우 정답 리스트에 넣기
    if vow >= 1 and con >= 2:
        ans.append(result)

# 개행문자를 이용해 리스트 한 줄에 출력
print(*ans, sep='\n')
