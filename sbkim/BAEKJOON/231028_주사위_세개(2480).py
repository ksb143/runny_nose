dices = list(map(int, input().split()))

dice_dict = {}

for i in range(1, 7):
    dice_dict[i] = 0

for num in dices:
    dice_dict[num] += 1


for key, value in dice_dict.items():
    if value == 3:
        reward = 10000 + key * 1000
        break
    elif value == 2:
        reward = 1000 + key * 100
        break
    elif value == 1:
        reward = key * 100


print(reward)
