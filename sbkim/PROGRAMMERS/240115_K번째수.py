# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때,
# k번째에 있는 수를 구하려 합니다.

# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때,
# commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때
# 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# array의 길이는 1 이상 100 이하입니다.
# array의 각 원소는 1 이상 100 이하입니다.
# commands의 길이는 1 이상 50 이하입니다.
# commands의 각 원소는 길이가 3입니다.


# array 뽑아낼 배열
# commands i, j, k 원소 가진 2차원 배열
def solution(array, commands):
    # 코멘드 길이 ㄱ
    len_comm = len(commands)
    answer = []
    return answer