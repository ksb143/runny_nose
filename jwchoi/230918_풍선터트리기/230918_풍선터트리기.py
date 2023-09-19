N = int(input())
b = list(map(int,input().split()))
# b에 적힌 숫자를 그냥 이용한후, 마지막에 원래번호로 바꿔주면 됨
# print(b)
idx = 0
pang = b.pop(idx) # 3
print(pang,b) # 3, [2,1,-3,-1]
idx = pang-1 # (1+)2 # 양수니깐 오른쪽 (1+)2칸감 * 양수일땐 idx = pang-1
pang = b.pop(idx) # -3
print(pang,b) # -3, [2,1,-1]
idx = pang # -3 # 음수니깐 왼쪽 3칸 감
pang = b.pop(idx) # -1
print(pang,b)