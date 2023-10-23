

# start 부터 시작해서 pick_num 개 고를 때까지 반복
def comb(start, cnt):

    # pick_num 개수까지 골랐으면 답 출력 후 탐색 중단
    if cnt == pick_num:
        # 오름차순으로 정렬 후 이미 추가하지 않았으면
        if sorted(chosen) not in result:
            # result 리스트에 정렬된 채로 추가해주기
            result.append(sorted(chosen))
            return
        # 이미 추가했을 경우 그냥 탐색 중단
        return

    # 시작 인덱스가 끝까지 도달하면 index error 방지하기 위해 탐색 중단
    if start == total_num + 1:
        return

    # numbers 내부를 start 부터 total_num 까지 돌면서 replace
    for num in range(start, total_num):
        # 이번 turn 에 사용하지 않은 숫자이면 선택하기
        if not visited[num]:
            chosen[start] = numbers[num]
            visited[num] = 1
            comb (start + 1, cnt + 1)
            visited[num] = 0


# total_num : 최대 숫자 개수, pick_num : 고를 숫자 개수
total_num, pick_num = map(int, input().split())

# 1 ~ total_num : 숫자들을 numbers 에 담음
numbers = [num for num in range(1, total_num + 1)]

# 오름차순으로 수열 골라서 출력하기
chosen = [-1] * pick_num

# 오름차순이므로 작은 수 -> 큰 수 방향으로만 이동
# 이전에 갔던 곳은 재방문하지 않도록 방문 표시 배열 만들기
visited = [0] * total_num

# 답을 중복제거 해서 오름차순으로 담을 list
result = []
comb(0, 0)

# 답을 형식에 맞게 출력하기 !
r = len(result)
for el in range(r):
    print(*result[el])