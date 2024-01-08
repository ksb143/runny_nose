# 민식이와 준영이는 자기 방에서 문자열을 공부하고 있다. 민식이가 말하길 인접해 있는 모든 문자가 같지 않은 문자열을 행운의 문자열이라고 한다고 한다.
# 준영이는 문자열 S를 분석하기 시작했다. 준영이는 문자열 S에 나오는 문자를 재배치하면 서로 다른 행운의 문자열이 몇 개 나오는지 궁금해졌다.
# 만약 원래 문자열 S도 행운의 문자열이라면 그것도 개수에 포함한다.

# 첫째 줄에 문자열 S가 주어진다. S의 길이는 최대 10이고, 알파벳 소문자로만 이루어져 있다.
from collections import defaultdict

S = input()
n = len(S)

lucky_word = [0] * n

cnt = 0
word_dict = defaultdict(int)
for s in S:
    word_dict[s] += 1


def perm(idx, n, word_dict, lucky_word):
    global cnt
    if idx == n:
        cnt += 1
        return

    for key in word_dict.keys():
        if word_dict[key] == 0 or (idx > 0 and key == lucky_word[idx-1]):
            continue
        # 해당 알파벳 사용
        word_dict[key] -= 1
        lucky_word[idx] = key
        # 재귀
        perm(idx+1, n, word_dict, lucky_word)
        # 해당 알파벳 되돌리기
        word_dict[key] += 1


perm(0, n, word_dict, lucky_word)

print(cnt)
