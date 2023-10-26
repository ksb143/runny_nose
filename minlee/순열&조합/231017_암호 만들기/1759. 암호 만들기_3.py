
def find_su(idx, final, m_cnt, s_cnt):
    if len(final) == L:
        # 조합이 다 만들어졌으면
        if m_cnt >= 1 and s_cnt >= 2:
            # 그리고 모음이 1개고 자음이 2개면
            final_answer = ''.join(final)
            # final에 들어가있는 문자들 하나로 만들어서 프린트
            print(final_answer)
        return

    if idx >= C:
        # 조합이 안만들어지는채로 인덱스가 계속 올라갈 수 있으니까
        # 인덱스 에러 방지 및 굳이 더 볼 필요 없는 거 보지 않겠다
        # 최종 주어진 문자 길이보다 커지면(+final에는 필요한만큼 담기지는 않음) 끝내기
        return

    if munja[idx] in 'aeiou': # 모음인지 확인
        find_su(idx + 1, final + [munja[idx]], m_cnt + 1, s_cnt)
        # 모음이면 모음이라고 표시하고, 답 lst(final)에 값 담아주고, 인덱스도 올려주기
        find_su(idx+1, final, m_cnt, s_cnt)
        # 선택하지 않는 문자일 때, 인덱스만 올려주기

    else: # 자음이면
        find_su(idx + 1, final + [munja[idx]], m_cnt, s_cnt + 1)
        # 자음이라고 표시하고, 답 lst(final)에 값 담아주고, 인덱스도 올려주기
        find_su(idx + 1, final, m_cnt, s_cnt)
        # 선택하지 않는 문자일 때, 인덱스만 올려주기


L, C = map(int, input().split())
munja = list(input().split())
munja.sort()
# 알파벳 순서대로 조합 만들거니까 미리 정렬해주기
visited = [0] * (C+1)
# 문자를 다 확인해볼거니까 문자 총 개수 생각하기

find_su(0, [], 0, 0)
# 빈 리스트부터 시작하기
