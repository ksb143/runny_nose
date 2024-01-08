N = int(input())
milk_stores = list(map(int, input().split()))

# 우유 차례
i = 0
# 먹을 우유 개수
cnt = 0
for milk in milk_stores:
    # 바나나 우유 먹을 차례
    if i % 3 == 0:
        # 먹으면 먹은 우유 개수 올리고 다음 차례 우유로 넘기김
        if milk == 0:  
            cnt += 1    
            i += 1
    # 딸기 우유 먹을 차례
    elif i % 3 == 1:
        # 먹으면 먹은 우유 개수 올리고 다음 차례 우유로 넘기김
        if milk == 1:
            cnt += 1
            i += 1
    # 초코 우유 먹을 차례
    elif i % 3 == 2:
        # 먹으면 먹은 우유 개수 올리고 다음 차례 우유로 넘기김
        if milk == 2:
            cnt += 1
            i += 1
print(cnt)