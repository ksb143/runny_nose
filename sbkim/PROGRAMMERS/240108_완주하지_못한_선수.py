# 수많은 마라톤 선수들이 마라톤에 참여하였습니다.
# 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다

# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

# 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.

# participant: 참여한 선수 이름이 담긴 배열
# completion이: 완주한 선수들의 이름이 담긴 배열
def solution(participant, completion):
    # 완주 선수를 체크하기 위한 딕셔너리 생성
    check = dict()
    # 참여자 선수 반복문
    for par in participant:
        # 딕셔너리에 해당 선수 이름이 있으면 인원 추가
        if par in check:
            check[par] += 1
        # 딕셔너리에 해당 선수 이름이 없으면 해당 선수 이름 한명 추가
        else:
            check[par] = 1

    # 완주자 인원을 한명씩 제외
    for com in completion:
        check[com] -= 1

    # 모두 다 제외된 딕셔너리에 남은 인원 1인 있으면 그 인원이 완주 못한 사람
    for key, value in check.items():
        if value == 1:
            answer = key
    return answer


# chat GPT 통한 효율화

# Counter 라이브러리
# iterable 객체의 각 요소의 등장 횟수 세고 딕셔너리로 반환
from collections import Counter

def solution(participant, completion):
    # 참여자와 완주자 목록의 각각의 요소 수를 세고 딕셔너리로 반환
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)


    # 참여자 목록에서 완주자 목록을 뺀 차집합 구하기 (키의 개수를 뺀 차집합 생성)
    answer_counter = participant_counter - completion_counter

    # 남은 참여자 중 한 명이 완주하지 못한 사람
    # 한 명만 남기 때문에 첫 번째 딕셔너리의 키를 구하면 됨
    answer = list(answer_counter.keys())[0]

    return answer
