from collections import defaultdict

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    ls = []
    for _ in range(N):
        ls.append(input().split())
    d = defaultdict(list)
    for key,val in ls:
        d[val].append(key)
    one = 1
    for i in d.keys():
        one *= (len(d[i])+1)
    print(one-1)
