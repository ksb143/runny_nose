from collections import deque
N = int(input()) # 5
b = list(map(int,input().split()))
di = {
    3: 1,
    2: 2,
    1: 3,
    -3: 4,
    -1: 5
}
# print('주어진배열: ',b)
# 규칙1: 0번 인덱스 풍선을 가장먼저 터뜨린다
# 규칙2: 풍선에 적힌 값(이후 '번호')만큼 이동한다(양:오른/음:왼)
# 규칙3: 이동시 이미 터진 풍선은 제외한다
b = deque(b)
# print('덱으로변경: ',b)
# 0번을 시작 인덱스로 설정한다

idx = b[0] # 0번 풍선의 번호를.. 새롭게 idx에 저장한다.!!!
result = di[idx]
print(result,end=" ") # 3(정답 시작)

b.popleft() # 터질 번호를 없앤다
b.rotate(N-idx)
# print(b) # deque([-3, -1, 2, 1])

idx = b[0]
result = di[idx]
print(result,end=" ")

b.popleft() # 터질 번호를 없앤다
b.rotate(idx)
# print(b) # deque([-1, 2, 1])

idx = b[0]
result = di[idx]
print(result,end=" ")

b.popleft()
b.rotate(idx)
# print(b)

idx = b[0]
result = di[idx]
print(result,end=" ")

b.popleft()
b.rotate(idx)

idx = b[0]
result = di[idx]
print(result,end=" ")