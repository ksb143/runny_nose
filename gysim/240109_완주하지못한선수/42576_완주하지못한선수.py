def solution(participant, completion):
    # participant : 마라톤에 참여한 선수들의 이름
    # completion : 완주한 선수들의 이름이 담긴 배열

    for player in completion:
        for p in range(len(participant)):
            if player == participant[p]:
                participant.pop(p)
                break

    answer = participant[0]
    return answer
