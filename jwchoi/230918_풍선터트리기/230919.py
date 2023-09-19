from collections import deque

# #비어있는 덱 만들기
# deque = deque()
# # 원소가 있는 덱 만들기
# # deque = deque([1,2,3])
#
# deque.appendleft(1) # 왼쪽 끝에 더함
# deque.append(2) # 오른쪽 끝에 더함
# deque.append(3) # 오른쪽 끝에 더함
# print(deque)
# deque.popleft() # 왼쪽 끝을 터트림
# deque.popleft() # 왼쪽 끝을 터트림
# deque.pop() # 오른쪽 끝을 터트림
# print(deque)
# # deque = deque(maxlen=5) # 최대길이를 명시하기(좀 중요기능)
# deque.extend(['l','o','v','e']) # 오른쪽 끝에 1,2,3 순으로 넣기
# print(deque)
# deque.extendleft(['y','o','u']) # 왼쪽 끝에 6,5,4 순으로 넣기
# print(deque)

# ----------------------------
# deque = deque('love')
# deque.insert(0,'K') # 0번 인덱스에 아이템 하나 추가하기
# print(deque)
# deque.insert(6,'K') # 6번 인덱스가 없을경우, 자동으로 맨끝에 아이템을 추가함
# print(deque)
# deque.remove('K') # 맨앞에 오는 'K' 아이템을 제거함
# print(deque)
# --------------------------------
test = [3,2,1,-3,-1]
test = deque(test)
test.rotate(-3)
print(test) # deque([-3, -1, 3, 2, 1]).. 왼쪽으로 3번 돈 결과가 나옴
test.rotate(3)
print(test) # deque([3, 2, 1, -3, -1]).. 오른쪽으로 3번 돈 결과가 나옴
test.clear()
print(test)