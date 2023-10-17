# https://docs.python.org/ko/3.8/library/itertools.html

from itertools import combinations

# L은 암호의 길이, C는 주어지는 문자의 총 개수
L, C = map(int, input().split())
# 알파벳 소문자로 이루어진 배열, 중복 없음
alphabets = input().split()
# 알파벳을 증가하는 순서로 정렬
alphabets.sort()

# 암호는 최소 한개의 모음(a, e, i, o, u)과 최소 두개의 자음으로 구성
# 가능성 있는 암호를 한줄에 하나씩 출력

# combinations(조합할 배열, 고를 개수) -> 반환값은 튜플 형태
for passwords in combinations(alphabets, L):
    cnt = 0     # 모음의 개수

    # 튜플 안에 있는 글자가
    for word in passwords:
        # 모음이면
        if word in 'aeiou':
            cnt += 1

    # 최소 한개의 모음, 최소 두개의 자음인지 확인
    # 자음의 개수 = 총 암호의 길이 L에서 모음의 개수 cnt를 뺀 것
    if cnt >= 1 and L - cnt >= 2:
        # 문자열로 합치기
        print(''.join(passwords))
