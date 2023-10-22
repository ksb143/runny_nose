# L은 암호의 길이, C는 주어지는 문자의 총 개수
L, C = map(int, input().split())
# 알파벳 소문자로 이루어진 배열, 중복 없음
alphabets = input().split()

# 알파벳을 증가하는 순서로 정렬
alphabets.sort()

# 암호는 최소 한개의 모음(a, e, i, o, u)과 최소 두개의 자음으로 구성
# 가능성 있는 암호를 한줄에 하나씩 출력

visited = [0] * C       # 사용여부 표시할 배열 -> 문자의 총 개수만큼 만들기
selected = [None] * L   # 고른 문자를 넣어줄 배열 -> 암호의 길이만큼 만들기


# 조합 함수, i는 인덱스, cnt는 고른 숫자의 개수
def comb(i, cnt):
    # 고른 숫자가 암호의 길이와 같으면
    if cnt == L:
        # 최소 한개의 모음, 최소 두개의 자음인지 확인
        # num_v =0
        # for i in 'aeiou':
        #     num_v += selected.count(i)
            
        numa = selected.count('a')
        nume = selected.count('e')
        numi = selected.count('i')
        numo = selected.count('o')
        numu = selected.count('u')
        # sum_v는 모음의 개수
        sum_v = numa + nume + numi + numo + numu
        # 자음의 개수 = 총 암호의 길이 L에서 모음의 개수 sum_v를 뺀 것
        if sum_v > 0 and L-sum_v > 1:
            # 문자열로 합치기
            print(''.join(selected))
        return

    # L개만큼 못 골랐는데 배열의 끝까지 왔으면
    if i == C:
        # 돌아가기
        return

    # selected에 현재 인덱스 i의 알파벳 넣어주기
    selected[cnt] = alphabets[i]
    # 조합 재귀 구현
    visited[i] = 1
    comb(i+1, cnt+1)
    visited[i] = 0
    comb(i+1, cnt)


comb(0, 0)
