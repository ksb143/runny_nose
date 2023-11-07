N = int(input())
for i in range(N):
    vine = list(input())
    monkey_max = 0
    # 괄호마다 값 표시해주기 위한 변수
    answer = 0
    # 답에 직접적으로 이용할 변수
    for k in vine:
        # 하나씩 순회하면서 파악하기
        if k == '[':
            monkey_max += 1
            # 최대로 연결된 것을 찾기위해 +1씩 해준다.
            # 최대로 내려가는 깊이가 바로 [[[[[이렇게 된걸 찾는 건데
        else:
            monkey_max -= 1
            # 만약 중간에 [] 이런 표시가 있다면 깊이 내려간 것인지 아닌것인지에 따라 달라지니까
            # 최대로 내려간 곳을 찾기 위해서는 잠시 []된 것 삭제하기 위해 -1을 써준다!
        if monkey_max > answer:
            answer = monkey_max
            # 최대값일때 값 위에 덮기
    print(2**answer)
    # 내려갈 때마다 2의 배수승으로 원숭이들이 나눠진다(가지치기라서!)

# ----------------------------------------------------------------------------------------------------------------
# 거꾸로 뒤집어서 푸니까 더 빨리 더 적은 메모리로 풀렸다. 그 이유는 무엇일까?
N = int(input())
for i in range(N):
    vine = list(input())
    vine.reverse()
    monkey_max = 0
    answer = 0
    # [ 이거는 +1, ] 이거는 -1, 계산해서 최대값 담기
    for k in vine:
        if k == '[':
            monkey_max -= 1
        else:
            monkey_max += 1
        if monkey_max > answer:
            answer = monkey_max
    print(2**answer)