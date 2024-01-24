count = 0
# 전부 다 보고 비교해야하니까 DFS를 사용해야한다
def DFS(calcul, point, numbers, target):
    # calcul은 계산식(숫자 증가시키면서 계산하는 것)
    # point는 numbers의 인덱스! 숫자들 얼만큼 사용했는지 알아보기 위해
    # numbers, target은 원래 주어지는 것
    global count
    # 답이 전체 몇 개인지 알아보는 변수
    if point == len(numbers):
        # numbers 전부 다 사용했을때
        if target == calcul:
            # target과 계산한 것이 동일하다면
            count += 1
            # 답 개수 추가
        return
    DFS(calcul + numbers[point], point+1, numbers, target)
    # 계산식 진행하기(+, - 각각)
    DFS(calcul - numbers[point], point+1, numbers, target)

def solution(numbers, target):
    global count
    DFS(0, 0, numbers, target)
    return count


# 좋아서 남겨보는 남의 풀이
def solution(numbers, target):
    if not numbers and target == 0:
        # numbers에 아무것도 없다는 건 다 잘라낸 거니까
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# 내꺼랑 혼합한 수정 풀이
def solution(numbers, target, index=0):
    if index == len(numbers):
        if target == 0:
            return 1
        else:
            return 0
    else:
        return solution(numbers, target - numbers[index], index + 1) + solution(numbers, target + numbers[index], index + 1)
