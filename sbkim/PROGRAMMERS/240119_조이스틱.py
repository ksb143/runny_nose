def solution(name):
    # name의 길이 알기
    N = len(name)
    # 조이스틱 움직인 숫자
    cnt = 0
    # A 판별
    check = False
    for i in range(N):
        # 연속 A인지 확인
        if i != 0 and name[i] == 'A':
            check = True
        # A에 더 가까울 경우
        if 78 > ord(name[i]):
            cnt += (ord(name[i]) - 65)
        # A에 더 먼 경우
        else:
            cnt += 91 - (ord(name[i]))
        # 연속 A인 경우 해당 길이만큼 안가도 되니까 빼기
        if check == True:
            cnt -= 1
    cnt += N - 1
    return cnt

solution("JAN")