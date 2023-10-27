# SWEA A형 대비 문제 숫자만들기 참고함

# 인접해 있는 모든 문자가 같지 않은 문자열을 행운의 문자열이라고 한다.
# 문자열 S에 나오는 문자를 재배치했을 때 서로 다른 행운의 문자열이 몇 개인지 출력

S = input()     # 알파벳 소문자로만 이루어진 문자열, 최대 길이는 10
N = len(S)      # 문자열 길이

alphabets = {}      # 알파벳이 몇번 나오는 지 넣어줄 빈 딕셔너리
for alpha in S:     # 문자열 순회하면서
    # 알파벳이 딕셔너리 안에 없으면
    if alpha not in alphabets:
        alphabets[alpha] = 1    # 초기값으로 1 설정
    # 알파벳이 딕셔너리 안에 있으면
    else:
        alphabets[alpha] += 1   # 개수 1 더해줌


# cnt : 뽑은 문자의 개수, before : 직전에 뽑은 문자
def comb(cnt, before):
    global ans

    # 문자열을 N 개만큼 뽑았으면
    if cnt == N:
        # 서로 다른 문자열 개수 +1
        ans += 1
        return

    # 알파벳 딕셔너리 안의 키를 순회하면서
    for key in alphabets.keys():
        # 사용할 숫자가 남아있고, 직전에 뽑은 문자랑 키가 다르면
        if alphabets[key] > 0 and key != before:
            # 해당 알파벳은 1개 사용함
            alphabets[key] -= 1
            # 다음 문자 뽑으러 가기
            comb(cnt+1, key)
            # 사용한 문자 다시 추가해주기
            alphabets[key] += 1


ans = 0         # 서로 다른 문자열의 개수
comb(0, '')     # 함수 실행

print(ans)
