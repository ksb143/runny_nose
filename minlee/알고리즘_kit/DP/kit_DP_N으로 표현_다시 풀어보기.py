# 스터디
# DP는 재귀로 풀지 않는다..?! 들어갔다가 반환하는 거 아니고
# 재귀의 반대! 앞의 것들부터 하나씩 채워나가는 느낌으로!
# 점화식, 완탐느낌으로,,
# 수학으로 풀어야 한다!
# 탑다운, 메모리제이션 둘 중 하나로 풀기..!

cnt = 9
def mix_operation(n, N, number, count):
    # 카운터가 8이 되는지 확인해보고
    global cnt
    if count > cnt:
        return
    if count > 8:
        return -1
    # number 이랑 계산한 값이랑 같은지 확인, 같으면 카운트 반환
    if eval(n) == number:
        if count < cnt:
            print(n)
            cnt = count
        return
    # [+, -, /, %, 붙이기] 한 거 넣기
    mix_operation(n+'+'+N, N, number, count + 1)
    mix_operation(n+'-'+N, N, number, count + 1)
    mix_operation(n+'*'+N, N, number, count + 1)
    mix_operation(n+'//'+N, N, number, count + 1)
    mix_operation(n+N, N, number, count + 1)
    # mix_operation(n*10+N, N, number, count + 1)

def solution(N, number):
    global cnt
    answer = set()
    n=str(N)
    mix_operation(n, n, number, 1)
    # answer.add(mix_operation(N, N, number, 0))
    if -1 in answer:
        answer.remove(-1)
    if cnt == 9 :
        cnt = -1
    return cnt

print(solution(5, 12)) # 4
print(solution(2, 11)) # 3

#
# cnt = 9
# a="5+5"
# b=int(a)
# def mix_operation(n, N, number, count):
#     global cnt
#     if count > 8:  # 8보다 크면 더 이상 탐색하지 않도록 수정
#         return
#     if n == number:
#         if count < cnt:
#             cnt = count
#         return
#
#     # 덧셈, 뺄셈, 곱셈 연산만 고려
#     mix_operation(n + N, N, number, count + 1)
#     mix_operation(n - N, N, number, count + 1)
#     mix_operation(n * N, N, number, count + 1)
#
#     if N != 0:
#         mix_operation(int(n / N), N, number, count + 1)
#
#     mix_operation(int(str(n) + str(N)), N, number, count + 1)
#
# def solution(N, number):
#     global cnt
#     mix_operation(N, N, number, 1)
#
#     if cnt == 9:
#         cnt = -1
#
#     return cnt

