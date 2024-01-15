def solution(array, commands):
    answer = []
    for arr in commands:
        i, j, k = arr[0]-1, arr[1]-1, arr[2]-1
        temp = array[i:j+1]
        temp.sort()
        answer.append(temp[k])

    return answer


# 한줄로 pythonic하게 푸는 방법
def solution2(array, commands):
    return list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2] - 1], commands))


# 한줄로 pythonic하게 푸는 방법2
def solution3(array, commands):
    return [sorted(array[a-1:b])[c-1] for a, b, c in commands]


# 가독성 좋으면서 간결한 코드
def solution4(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer
