def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    # ok = 학생 당 가질 수 있는 체육복 개수 리스트
    ok = [1]*(n+1)
    ok[0] = 0
    # 도난당한 경우 체육복 개수 -1
    for lo in lost:
        ok[lo] -= 1
    # 여유분 있는 경우 체육복 개수 +1
    for rsv in reserve:
        ok[rsv] += 1
    # 여유분 있는 사람이 도난당한 옆 번호에게 빌려주기
    for idx in range(1, n+1):
        # 해당 번호 학생이 체육복이 없을 경우
        if ok[idx] == 0:
            # 1번은 2번에게만 빌릴 수 있음
            if idx == 1:
                if ok[2] >= 2:
                    ok[1] += 1
                    ok[2] -= 1
            # n번은 n-1번에게만 빌릴 수 있음
            elif idx == n:
                if ok[n-1] >= 2:
                    ok[n] += 1
                    ok[n-1] -= 1
            # 만약 한 학생이 체육복을 빌릴 수 있는 두 명의 학생(앞번호와 뒷번호) 사이에 있고, 
            # 두 학생 모두 여벌의 체육복이 있다면, 
            elif idx > 1 and idx < n:
                if ok[idx-1] >= 2:
                    ok[idx] += 1
                    ok[idx-1] -= 1
                elif ok[idx+1] >= 2:
                    ok[idx] += 1
                    ok[idx+1] -= 1
    cnt = 0
    for student in range(1, n+1):
        if ok[student] >= 1:
            cnt += 1
    return cnt