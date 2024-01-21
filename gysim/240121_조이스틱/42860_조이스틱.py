# 맨 처음엔 A로만 이루어져 있음, 세글자인 경우 AAA, 네글자인 경우 AAAA


def solution(name):
    answer = 0

    n = len(name)   # 문자열 길이

    for i in range(n):
        # 알파벳 만들기
        if ord(name[i]) <= 78:
            answer += (ord(name[i])-ord('A'))
        else:
            answer += 26 - (ord(name[i])-ord('A'))

    idx = 0  # 현재 커서 위치
    for i in range(1, n):
        if name[i] == 'A':
            continue
        else:
            answer += min(i - idx, 3 - (i - idx))
            idx = i

    return answer


print(ord('A'))  # 65
print(ord('N'))  # 78
print(ord('Z'))  # 90

solution("JEROEN")
