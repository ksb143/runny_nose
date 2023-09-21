# 유사한 느낌의 문제: 백준_유기농배추, 백준_미로탐색
# 유사한 개념: BFS(너비우선검색)-> 큐/덱 쓰기
from collections import deque
m,n = map(int,input().split())
data  = [list(map(int,input().split()))for _ in range(n)]
