word = input()
# 알파벳 세개로 이루어진 것은 예외처리 어려우니 미리 바꿔주기
word = word.replace('dz=', 'dž')
word = list(word)

N = len(word)
cnt = 0
i = 0

# 해당 알파벳 다 돌 때까지 판단
while i != N:
    if i <= N-2:
        # 크로아티아 알파벳으로 구성된 것 판단
        cr = word[i] + word[i+1]
        if cr == 'c=' or cr == 'c-' or cr == 'd-' or cr == 'lj' or\
            cr == 'nj' or cr == 's=' or cr == 'z=' or cr == 'dž':
            cnt += 1
            i += 2
        # 크로아티아 알파벳 아닐 경우
        else:
            cnt += 1
            i += 1
    # 범위에 맞지 않는 경우 그냥 알파벳임으로 하나 추가
    else:
        cnt += 1
        i += 1
print(cnt)

