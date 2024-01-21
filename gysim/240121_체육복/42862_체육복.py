# 바로 앞번호 학생이나 바로 뒷번호 학생에게만 빌려 줄 수 있다
# 전체 학생 수 n, 도난당한 학생 번호 배열 lost, 여벌 학생 번호 reserve
# return 학생의 최댓값

def solution(n, lost, reserve):
    answer = 0

    lost.sort()
    reserve.sort()

    sold = []
    temp = []

    # 여벌 있는 학생이 도난당한 경우 reserve 에서 제거
    for l in lost:
        if l in reserve:
            temp.append(l)
            reserve.remove(l)

    for t in temp:
        if t in lost:
            lost.remove(t)

    # 앞 뒤 확인
    for l in lost:
        if (l - 1) in reserve and (l - 1) not in sold:
            sold.append(l - 1)

        elif (l + 1) in reserve and (l + 1) not in sold:
            sold.append(l + 1)

    return n - len(lost) + len(sold)


# 내 코드를 개선한 코드
def solution2(n, lost, reserve):
    # 정렬하기
    lost.sort()
    reserve.sort()


    # 여벌 있는 학생이 도난당한 경우 lost, reserve 에서 제거
    for i in range(1, n + 1):
        if i in lost and i in reserve:
            reserve.remove(i)
            lost.remove(i)

    sold = []  # 이미 빌려준 학생
    # 앞 뒤 확인
    for l in lost:
        if (l - 1) in reserve and (l - 1) not in sold:
            sold.append(l - 1)

        elif (l + 1) in reserve and (l + 1) not in sold:
            sold.append(l + 1)

    return n - len(lost) + len(sold)


# pythonic 한 코드
def solution3(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)


# 이해하기 쉬운 코드
def solution4(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    for i in range(1, n+1):
        if i not in lost: #안 잃어버린 학생
            answer += 1
        else:
            if i in reserve: #잃어버렸지만 여분도 있는 학생
                answer += 1
                reserve.remove(i)
                lost.remove(i)

    for i in lost: #잃어버리고 여분도 없어서 빌려야 하는 학생
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)

        elif i+1 in reserve:
            answer +=1
            reserve.remove(i+1)

    return answer