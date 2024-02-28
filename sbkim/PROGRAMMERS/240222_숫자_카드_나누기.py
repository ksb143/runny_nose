def solution(arrayA, arrayB):
    # 최대값 통해서 모든 경우의 수 확인
    max_a = max(arrayA)
    # arrayA 공약수 넣을 세트
    divider_a = set()
    # arrayA 공약수 구하기
    for i in range(2, max_a+1):
        for num in arrayA:
            # 나뉘어지지 않으면 탈락
            if num % i != 0:
                break
        else:
            divider_a.add(i)
    # 최대값 통해서 모든 경우의 수 확인
    max_b = max(arrayB)
    # arrayB 공약수 넣을 세트
    divider_b = set()
    # arrayB 공약수 구하기
    for i in range(2, max_a+1):
        for num in arrayB:
            # 나뉘어지지 않으면 탈락
            if num % i != 0:
                break
        else:
            divider_b.add(i)
    check_a = -1
    value = 0
    # 리스트 확인
    for num_a in list(divider_a):
        if num_a not in divider_b:
            print(num_a)
            if value < num_a:
                value = num_a
    for num_b in list(divider_b):
        if num_b not in divider_a:
            print(num_b)
            if value < num_b:
                value = num_b
    return value

solution([10, 17], [5, 20])