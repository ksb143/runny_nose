T = int(input())
for tc in range(1, T+1):
    # N: 숫자의 개수, K: 크기 순서
    N, K = map(int, input().split())
    # 일단 input()으로 받음, 요구사항에 따라 리스트로 변경할 수도 있음
    # data : 16진수 숫자 문자열
    data = input()

    # 한변의 길이는 N//4 -> 비밀번호의 길이
    # 문자열 순서대로 한칸씩 이동하면서 N//4만큼 문자열 뽑아서 새로운 배열에 넣기
    result = []

    # 숫자를 연결해야하니까 모듈러 사용해야됨
    # 몇번 반복? -> N 또는 N//4
    # 중복 제거 -> 답을 리스트에 담아서 not in list이면 append 하기
    for i in range(N):
        tmp = ''
        for j in range(i, i+N//4):
            tmp += data[(j+1)%N]

        if tmp not in result:
            result.append(tmp)

    # 보물상자에 적힌 숫자로 만들 수 있는 수 중 K번째로 큰 수를 10진수로 만든 수
    ans = []
    for i in range(len(result)):
        ans.append(int(result[i], 16))

    # 내림차순 정렬
    ans.sort(reverse=True)

    # K번째 큰 수이기 때문에 인덱스는 K-1
    print(f'#{tc} {ans[K-1]}')
