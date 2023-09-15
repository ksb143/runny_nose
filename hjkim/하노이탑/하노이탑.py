def hanoi(i,N)

N = int(input())
stick = [1, 2, 3]
circle = [x for x in range(1, N+1)]
# print(stick) [1, 2, 3]
# print(circle) [1, 2, 3]

'''
K : 옮긴 횟수 출력
수행 과정 출력
A1 B1     (A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다)
A2 B2
...
Ak Bk   (총 K 줄 출력)
'''
'''
input 3

output
7
1 3
1 2
3 2
1 3
2 1
2 3
1 3
'''