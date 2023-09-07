T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    number = list(input())
    # rotate 횟수
    r = N // 4
    # passwords 후보군 세트
    passwords = set()
    
    # 돌리고 넣어주기
    for i in range(r):
        for j in range(i, i+N, r):
            num = ''
            for k in range(r):
                num += number[(j+k)%N]
            passwords.add(int(num, 16))

    # 리스트화, 내림차순
    passwords = sorted(list(passwords), reverse = True)
    ans = passwords[K-1]
    print(f'#{tc} {ans}')
    