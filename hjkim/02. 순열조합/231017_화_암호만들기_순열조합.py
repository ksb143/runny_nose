

def password(idx, cnt):
    
    # 뽑은 개수가 pick_num 개수면 그만 뽑기
    if cnt == pick_num:
        print("".join(answer))
        return
    
    # Index Error 방지용
    if idx == total_num:
        return

    # alphabet : words 내부에 있는 알파벳 하나씩 고르는 인덱스
    for alphabet in range(idx, total_num):
        # 답에 추가하기
        answer.append(words[alphabet])
        # 골랐으면 다음으로 넘어가기 - 다음번 알파벳부터 시작, cnt 하나씩 올려주기
        password(alphabet + 1, cnt + 1)
        # 정답에서 빼놓기
        answer.pop()
    

pick_num, total_num = map(int, input().split())
# pick_num : 뽑을 알파벳 개수 , total_num : 주어진 전체 알파벳 개수
# 4 6
# a t c i s w
words = sorted(list(input().split()))  
# 뽑은 것 중에 모음 1개 이상, 자음 2개 이상
vowels = ['a', 'e', 'i', 'o', 'u']     
answer = []
password(0, 0)
