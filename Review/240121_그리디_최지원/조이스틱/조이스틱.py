# 내 머리통으로 답이 안나와서, 챗지피티의 힘을 빌림.

def solution(name):
    # 상하 조작 횟수 계산
    vertical_moves = sum(min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1) for ch in name)

    # 좌우 이동 최소화: 연속된 'A'가 있는 가장 긴 시퀀스를 찾아 그 부분을 건너뜀
    # 이동 거리의 최소값 초기화
    min_move = len(name) - 1
    for i in range(len(name)):
        # 연속된 'A' 끝까지의 인덱스 탐색
        next_char = i + 1
        while next_char < len(name) and name[next_char] == 'A':
            next_char += 1

        # 최소 이동 거리 계산: 현재 위치까지 이동 + 현재 위치에서 다시 처음으로 돌아감 + 끝에서 연속된 A 이후의 문자까지의 이동
        move = min(i + i + len(name) - next_char, min_move)
        min_move = min(min_move, move)

    return vertical_moves + min_move

# 예제 "JAZ"에 대한 최소 이동 횟수 테스트
# solution("JAZ")
