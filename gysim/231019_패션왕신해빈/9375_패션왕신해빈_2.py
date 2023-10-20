# 모든 조합의 경우를 하나하나 구현하는게 아니라 경우의 수 "개수"만 구하면 된다
# -> 부분집합을 이용해서 푸는 것이 아니고 수학적으로 계산하기
# import sys
# input = sys.stdin.readline

tc = int(input())   # 테스트 케이스 수
for _ in range(tc):
    n = int(input())    # 해빈이가 가진 의상 수

    # 한 종류를 여러개 못 입는다 = 한 종류를 한개만 입거나 or 안입거나
    # 종류별로 한개만 골라서 입는 경우의 수는 어떻게 계산할까?
    # 1번 테케로 예를 들어보면 headgear는 2개, eyewear는 1개가 있다
    # headgear를 입는 경우는 안입기, hat, turban 3가지가 있고,
    # eyewear를 입는 경우는 안입기, sunglasses 2가지가 있다
    # 즉, 한 종류를 입는 경우의 수는 안입는 것까지 포함해야해서 (의상 개수 + 1) 이다
    # 모든 경우의 수 = (heargear를 입는 경우의 수) * (eyewear를 입는 경우의 수) 이다
    # 그런데 둘다 안입으면 알몸이 되기 때문에 알몸이 되는 경우 1가지를 빼줘야한다
    # 따라서, 점화식으로 표현하면 ans = (의상종류1 개수 + 1) * ... * (의상종류n 개수 + 1) - 1

    # 의상 정보를 넣어줄 빈 딕셔너리
    cloth_dict = {}
    # 의상 수 n만큼 반복하면서
    for i in range(n):
        # 의상이름, 의상종류 순서로 입력받음
        a, b = input().split()
        # 의상 이름은 필요없어서 a는 굳이 넣어줄 필요 없음
        # cloth_dict[b].append(a)
        # 만약 입력받은 의상종류가 딕셔너리 키에 있으면
        if b in cloth_dict.keys():
            # 원래 밸류 값에 1 증가시키기
            cloth_dict[b] += 1
        # 입력받은 의상종류가 딕셔너리 키에 없으면
        else:
            # 초기값으로 1 넣어주기
            cloth_dict[b] = 1

    # 곱하기 계산 할거라서 초기값은 1로 설정
    ans = 1
    # 딕셔너리에 있는 키를 모두 순회하면서
    for k in cloth_dict.keys():
        # 키에 해당하는 밸류값에 1을 더해서 곱해주기
        ans *= (cloth_dict[k] + 1)

    # 아무것도 안입는 경우의 수 빼주기
    print(ans-1)
