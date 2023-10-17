# L은 암호의 길이, C는 주어지는 문자의 총 개수
L, C = map(int, input().split())
# 알파벳 소문자로 이루어진 배열, 중복 없음
alphabets = input().split()

# 알파벳은 증가하는 순서로 정렬
alphabets.sort()

# 암호는 최소 한개의 모음(a, e, i, o, u)과 최소 두개의 자음으로 구성
# 가능성 있는 암호를 한줄에 하나씩 출력

visited = [0] * C
selected = [None] * L


def comb(i, cnt):
    if cnt == L:
        # 최소 한개의 모음, 최소 두개의 자음인지 확인
        numa = selected.count('a')
        nume = selected.count('e')
        numi = selected.count('i')
        numo = selected.count('o')
        numu = selected.count('u')
        sum_v = numa + nume + numi + numo + numu
        if sum_v > 0 and L-sum_v > 1:
            print(''.join(selected))
        return

    if i == C:
        return

    selected[cnt] = alphabets[i]
    visited[i] = 1
    comb(i+1, cnt+1)
    visited[i] = 0
    comb(i+1, cnt)


comb(0, 0)
