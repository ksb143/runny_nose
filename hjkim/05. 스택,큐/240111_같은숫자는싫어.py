def solution(arr):
    num = [arr[0]]
    for el in arr:
        if el != num[-1]:
            num.append(el)
    return num
