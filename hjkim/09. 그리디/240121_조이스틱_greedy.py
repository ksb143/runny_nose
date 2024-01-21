def solution(name):
    answer = 0
    N = len(name)
    tmp = [0] * N
    alphabet = {
        'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,
        'M':12,'N':13,'O':12,'P':11,'Q':10,'R':9,'S':8,'T':7,'U':6,'V':5,'W':4,
        'X':3,'Y':2,'Z':1
        }
    # 각 알파벳을 만들기 위해 움직여야 하는 횟수는 상수값
    for idx in range(N):
        if name[idx] in alphabet.keys():
            tmp[idx] = alphabet[name[idx]]
    answer += sum(tmp)
    # 커서를 가장 적게 움직이는 경우가 최소 이동임
    print(answer)
    print(tmp)