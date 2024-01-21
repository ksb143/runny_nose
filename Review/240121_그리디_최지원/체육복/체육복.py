# 기본, 변화1, 변화2 까진 잘 되었는데, 분배과정에서 현재사람의 왼쪽/오른쪽 나누기가 잘 되지 않았음.

def solution(n, lost, reserve):
    # 기본: 모든 학생들은 하나씩 옷을 가지고 있음.
    clothes = [1] * n

    # 변화1: 옷을 도난 당한 사람들(=옷거지)은 옷의 개수가 1 줄어듬
    for l in lost:
        clothes[l - 1] -= 1

    # 변화2: 여벌을 가진 사람들(=옷부자)은 옷의 개수가 1 늘어남
    for r in reserve:
        clothes[r - 1] += 1

    # 분배의 과정
    for i in range(n):
        if clothes[i] == 0:
            if i > 0 and clothes[i - 1] > 1: # 현재 위치의 왼쪽 사람이 옷부자이고, 현재 사람이 반대인 경우
                clothes[i - 1] -= 1 # 옷부자에게 옷이 1 줄어듬
                clothes[i] += 1     # 옷거지에게 옷이 1 늘어남
            elif i < n - 1 and clothes[i + 1] > 1: # 현재 위치의 오른쪽 사람이 옷부자이고, 현재사람이 반대인 경우
                clothes[i + 1] -= 1 # 옷부자에게 옷이 1 줄어듬
                clothes[i] += 1     # 옷거지에게 옷이 1 늘어남

    # 수업에 참여할 수 있는 학생 수 계산
    return len([c for c in clothes if c > 0])
