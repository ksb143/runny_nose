def solution(array, commands):
    l = array[commands[0][0]:commands[0][1]+1]
    l.sort()
    print(l[commands[0][2]])
    return

array0, commands0 = [1,5,2,6,3,7,4]	,[[2,5,3], [4,4,1], [1,7,3]]

print(solution(array0,commands0))