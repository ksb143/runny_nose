

def pick(index, total, sum_v):
    if index == total + 1:
        result.add(sum_v)
        return



    for num in range(4):
        sum_v += roman_num[num]
        pick(index + 1, total, sum_v)
        sum_v -= roman_num[num]


N = int(input())
roman_num = [1, 5, 10, 50]
result = set()
pick(1, N, 0)
print(len(result))