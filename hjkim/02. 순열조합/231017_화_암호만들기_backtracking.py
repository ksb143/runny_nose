# https://fre2-dom.tistory.com/454
# 백트래킹 풀이 소개

def password(idx, cnt):

    global answer

    # 암호를 만들었을 때
    if cnt == l:
        # 모음, 자음 체크
        cnt_v, cnt_c = 0, 0

        for alphabet in range(l):
            if answer[alphabet] in vowels:
                cnt_v += 1
            else:
                cnt_c += 1

        # 모음 1개 이상, 자음 2개 이상
        if cnt_v >= 1 and cnt_c >= 2:
            print("".join(answer))

        return

    # 반복문을 통해 암호를 만든다.
    for i in range(idx, c):
        answer.append(words[i])
        password(i + 1, cnt + 1)
        answer.pop()


l, c = map(int, input().split())
words = sorted(list(input().split()))  # l : 뽑을 알파벳 개수 , c : 주어진 전체 알파벳 개수
vowels = ['a', 'e', 'i', 'o', 'u']     # 뽑은 것 중에 모음 1개 이상
answer = []
password(0, 0)