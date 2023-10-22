# https://velog.io/@mjieun/Python-순열조합중복순열중복조합부분집합-구현하기-with-재귀

# 뽑을 숫자 개수
N = int(input())

# 4가지 로마숫자를 중복은 허용, 순서는 상관없이 N개 뽑는 조합

# 로마숫자에 해당하는 값 저장, 편의상 키를 숫자로 설정
roms = {'0': 1, '1': 5, '2': 10, '3': 50}
nums = set()    # 뽑은 로마숫자를 더해서 넣어줄 세트
visited = [0] * 4   # 뽑은 숫자 개수를 저장할 배열


# start는 탐색을 시작할 인덱스, cnt는 뽑은 숫자의 개수
def comb(start, cnt):
    # 숫자를 N개 뽑았으면
    if cnt == N:
        sum_v = 0   # 로마숫자 더해줄 변수
        # visited 배열 순회
        for v in range(4):
            # visited에 저장된 값이 0이 아니면
            if visited[v]:
                # visited에 저장된 뽑은 숫자 개수와 인덱스 v에 해당하는 로마숫자를 곱해서 더해주기
                sum_v += roms[str(v)] * visited[v]
        # 계산한 값을 세트에 넣어주기
        nums.add(sum_v)
        return

    # start부터 3까지 범위 내에서
    for i in range(start, 4):
        # 누적해서 더해주면 뽑은 카드의 개수가 저장됨
        visited[i] += 1
        # 다음 숫자 살펴볼 인덱스는 i부터 시작, 뽑은 숫자 개수 1 더해줌
        comb(i, cnt+1)
        # 뽑은 개수의 카드 빼주기
        visited[i] -= 1


comb(0, 0)
# 세트의 길이는 곧 서로 다른 수의 개수
print(len(nums))
