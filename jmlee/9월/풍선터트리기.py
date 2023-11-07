'''
5
3 2 1 -3 -1
'''

N = int(input())        # 자연수 : 풍선 갯수
data = list(map(int, input().split()))  # 풍선안에 적힌 수

# data의 1번 풍선을 무조건 첫번째로 터트려 (시작점)
start = 0
info = data[0]          # 3 
data.pop(0)             # [2, 1, -3, -1]

result = []
# data가 비어있지 않으면 계속 돌려
while True:
    # 만약 info가 양수라면
    if info > 0:
        start = info-1
        # info 번째 data를 info에 넣고
        info = data[start]
        # pop해
        data.pop(start)
        result.append()
    # 만약 info가 홀수라면
    else:
        start = info-1
        data.pop(info)
        info = data[abs(data[start])]
    
