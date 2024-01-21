# 조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
# ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA
#
# 조이스틱을 각 방향으로 움직이면 아래와 같습니다.
#
# ▲ - 다음 알파벳
# ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
# ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
# ▶ - 커서를 오른쪽으로 이동 (마지막 위치에서 오른쪽으로 이동하면 첫 번째 문자에 커서)
# 예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.
#
# - 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
# - 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
# - 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
# 따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
# 만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.
#
# 제한 사항
# name은 알파벳 대문자로만 이루어져 있습니다.
# name의 길이는 1 이상 20 이하입니다.

def solution(name):
    # 여기에 정답 넣을 거
    count = 0
    # 커서 이동(정방향 / A를 중간에 만났을 때 돌아서 가는 거)
    count_std = len(name) - 1
    for num in range(1, len(name)+1):
        if name[-num] == 'A':
            count_std -= 1
            continue
        break
    # 커서 이동(A를 중간에 만났을 때 돌아서 가는 거) # 미완성
    count_back = 0
    for idx in range(0, len(name)):
        for num in range(idx, len(name)):
            if name[num] == "A":
                count_back += 1
                continue
            min(count_std, count_back)
            break
    # 숫자 넣기
    for i in name:
        count += ord(i) - 65 if ord(i) < 78 else (90 - ord(i)+1)
    return count

# ord(A) = 65, chr(65) = A

print(solution("JEROEN")) # 56
print(solution("JAN")) # 23


# 다른 사람 답
def solution(name):
    answer = 0
    min_move = len(name) - 1
    next = 0
    while name[min_move] == 'A' and min_move > 0:
        min_move -= 1
    if (min_move < 0):
        return answer
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        next = i + 1
        for j in range(i, len(name)):
            if name[j] == "A":
                next += 1
                continue
            break
        while next < len(name) and name[next] == 'A':
            next += 1
        min_move = min(min_move, i + i + (len(name) - next))
    answer += min_move
    return answer