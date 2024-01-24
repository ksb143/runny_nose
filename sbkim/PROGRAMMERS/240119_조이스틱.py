# 조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.

# ▲ - 다음 알파벳
# ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
# ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
# ▶ - 커서를 오른쪽으로 이동 (마지막 위치에서 오른쪽으로 이동하면 첫 번째 문자에 커서)

# 만들고자 하는 이름 name이 매개변수로 주어질 때,
# 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

# 제한사항
# name은 알파벳 대문자로만 이루어져 있습니다.
# name의 길이는 1 이상 20 이하입니다.

# ord('A') = 65
# ord('Z') = 90
# 중간 숫자 78

# 실패1 (왔다리 갔다리 해도 적은 수로 이동할 수 있는 걸 생각 못함)
def solution1(name):
    # name의 길이 알기
    N = len(name)
    # 바꿔야 할 문자 리스트화
    name = list(name)
    # 기존 문자 리스트화
    word1 = ['A'] * N
    word2 = ['A'] * N
    # 일단 첫글자는 미리 바꿔주기
    word1[0] = name[0]
    word2[0] = name[0]
    # 조이스틱 움직인 숫자
    cnt1 = min((ord(name[0]) - 65), (91 - ord(name[0])))
    cnt2 = min((ord(name[0]) - 65), (91 - ord(name[0])))
    # 조이스틱 및 커서 움직이기 정방향
    for i in range(1, N):
        # 바꿘 word가 name과 같다면 break
        if word1 == name:
            break
        # 알파벳 이동 횟수
        cnt1 += min((ord(name[i]) - 65), (91 - ord(name[i])))
        # 알파벳 이동했으니 기존 글자 바꿔주기
        word1[i] = name[i]
        # 커서 옮기기
        cnt1 += 1
    # 조이스틱 및 커서 움직이기 역방향
    for i in range(1, N):
        # 바꿘 word가 name과 같다면 break
        if word2 == name:
            break
        # 알파벳 이동 횟수
        cnt2 += min((ord(name[-i]) - 65), (91 - ord(name[-i])))
        # 알파벳 이동했으니 기존 글자 바꿔주기
        word2[-i] = name[-i]
        # 커서 옮기기
        cnt2 += 1
    cnt = min(cnt1, cnt2)
    return cnt

# 실패2 (왔다리 갔다리 해도 적은 수로 이동할 수 있는 걸 생각 못함)
def solution2(name):
    # name의 길이 알기
    N = len(name)
    # 알파벳 숫자로 바꾸기
    lst = []
    for i in range(N):
        # 알파벳 이동 횟수
        lst.append(min((ord(name[i]) - 65), (91 - ord(name[i]))))
    # 알파벳 이동 횟수 cnt에 넣기
    cnt = sum(lst)
    # 첫 글자는 무조건 방문하니까 0 고정
    lst[0] = 0
    # 정방향 방문
    straight = lst[:]
    st_cnt = 0
    for i in range(1, N):
        if sum(straight) == 0:
            break
        straight[i] = 0
        st_cnt += 1
    # 역방향 방문
    reverse = lst[:]
    rev_cnt = 0
    for i in range(1, N):
        if sum(reverse) == 0:
            break
        reverse[-i] = 0
        rev_cnt += 1
    # 정방향과 역방향 중 작은 것을 더하기
    cnt += min(st_cnt, rev_cnt)
    return cnt

# 실패3 (A로만 구성된 단어도 있다는 것을 생각 못함)
def solution3(name):
    # name의 길이 알기
    N = len(name)
    # A가 아닌 숫자 인덱스 집어넣을 배열
    idx_lst = []
    # 조이스틱 움직인 횟수
    cnt = 0
    for i in range(N):
        # 알파벳 이동 횟수
        move_num = min((ord(name[i]) - 65), (91 - ord(name[i])))
        cnt += move_num
        # 'A'가 아닐 경우 인덱스 집어넣기
        if move_num and i != 0:
            idx_lst.append(i)
    # 현재 위치 변수 (오른쪽으로 갈 것)
    right_position = 1
    right_cnt = 1
    right = idx_lst[:]
    while right:
        # 현재 위치 기준 거리를 집어 넣을 딕셔너리
        length = {}
        for ri in right:
            if ri <= right_position:
                length[ri] = min((right_position - ri), (N - right_position + ri))
            else:
                length[ri] = min((ri - right_position), (right_position + N - ri))
        min_v = 0xffffffff
        for key, value in length.items():
            if value < min_v:
                min_v = value
                right_position = key
        right.remove(right_position)
        right_cnt += min_v
    # 현재 위치 변수 (왼쪽으로 갈 것)
    left_position = N-1
    left_cnt = 1
    left = idx_lst[:]
    while left:
        # 현재 위치 기준 거리를 집어 넣을 딕셔너리
        length = {}
        for li in left:
            if li <= left_position:
                length[li] = min((left_position - li), (N - left_position + li))
            else:
                length[li] = min((li - left_position), (left_position + N - li))
        min_v = 0xffffffff
        for key, value in length.items():
            if value < min_v:
                min_v = value
                left_position = key
        left.remove(left_position)
        left_cnt += min_v
    cnt += min(right_cnt, left_cnt)
    return cnt

# 성공
def solution4(name):
    # name의 길이 알기
    N = len(name)

    # 모든 글자가 A일 경우 바로 완성되므로 바로 return
    current_state = 'A' * N
    if current_state == name:
        return 0

    # A가 아닌 숫자 인덱스 집어넣을 배열
    idx_lst = []
    # 조이스틱 움직인 횟수
    cnt = 0
    for i in range(N):
        # 알파벳 이동 횟수
        # A와 가까운지 Z와 가까운지 체크한다
        move_num = min((ord(name[i]) - 65), (91 - ord(name[i])))
        # 조이스틱 움직인 횟수
        cnt += move_num
        # 'A'가 아닐 경우 인덱스 집어넣기
        if move_num and i != 0:
            idx_lst.append(i)

    # 현재 위치 변수 (오른쪽으로 갈 것)
    right_position = 1
    right_cnt = 1
    # deepcopy 만드는 방법
    right = idx_lst[:]
    while right:
        # 현재 위치 기준 거리를 집어 넣을 딕셔너리
        length = {}
        for ri in right:
            if ri <= right_position:
                length[ri] = min((right_position - ri), (N - right_position + ri))
            else:
                length[ri] = min((ri - right_position), (right_position + N - ri))
        min_v = 0xffffffff
        for key, value in length.items():
            if value < min_v:
                min_v = value
                right_position = key
        right.remove(right_position)
        right_cnt += min_v

    # 현재 위치 변수 (왼쪽으로 갈 것)
    left_position = N-1
    left_cnt = 1
    left = idx_lst[:]
    while left:
        # 현재 위치 기준 거리를 집어 넣을 딕셔너리
        length = {}
        for li in left:
            if li <= left_position:
                length[li] = min((left_position - li), (N - left_position + li))
            else:
                length[li] = min((li - left_position), (left_position + N - li))
        min_v = 0xffffffff
        for key, value in length.items():
            if value < min_v:
                min_v = value
                left_position = key
        left.remove(left_position)
        left_cnt += min_v

    cnt += min(right_cnt, left_cnt)

    return cnt