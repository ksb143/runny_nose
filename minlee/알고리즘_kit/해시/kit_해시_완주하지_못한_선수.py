from collections import defaultdict

# 1번 방법 : defaultdict 사용하기
def solution(participant, completion):
    participant_dic = defaultdict(int)
    for i in participant:
        participant_dic[i] += 1
    for j in completion:
        participant_dic[j] -= 1
        if participant_dic[j] == 0:
            del(participant_dic[j])
    # for answer in participant_dic:
    #     return answer
    return list(participant_dic.keys())[0]

# 2번 방법 : 정렬 이용하기
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]

# 문제
# 수많은 마라톤 선수들이 마라톤에 참여하였습니다.
# 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# - 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# - completion의 길이는 participant의 길이보다 1 작습니다.
# - 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# - 참가자 중에는 동명이인이 있을 수 있습니다.

# 테스트 케이스
# solution(participant,	completion)
#
# solution(["leo", "kiki", "eden"],	["eden", "kiki"])
# "leo"
# solution(["marina", "josipa", "nikola", "vinko", "filipa"],	["josipa", "filipa", "marina", "nikola"])
# "vinko"
# print(solution(["mislav", "stanko", "mislav", "ana"],	["stanko", "ana", "mislav"]))
# "mislav"