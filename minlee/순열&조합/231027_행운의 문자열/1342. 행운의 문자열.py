# 순열 문제
# 동일한 문자열은 옆에 안오도록!
# 문자열을 리스트로 받아서 문자열 순회하면서 같은 글자 못오도록!
# 정렬하고 하나씩 뽑는데 다른 건 넘어가기!
def sunyeol(lst):
    global count
    if len(lst) == len(S):
        count += 1
        return
    for i in range(1, len(S)):
        if S[i] != S[i-1]:
            if not visited[i]:
                visited[i] = 1
                sunyeol(lst + [S[i]])
                visited[i] = 0


S = list(input())
# 문자열 받은 거
count = 1
# 총 몇 개의 행운의 문자열인지 카운트

answer = [S[0]]
# count_S = set(S)
# # 문자 종류 뽑아내기
# howmany = len(count_S)
# # 문자열 속 각 문자의 개수

visited = [1] + [0] * (len(S))
# 방문여부 확인용 리스트 만들기

sunyeol(answer)
print(count)