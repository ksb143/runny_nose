def solution(numbers, target):

    # DFS 로 접근
    # idx = 몇번째 operator 를 선택하는지
    # check_num = 만든 숫자


    def solve(idx, check_num):
        # 프로그래머스에서 풀이할 때는 global 대신 nonlocal 사용
        nonlocal answer
        # 모든 숫자를 선택한 이후에
        if idx == N:
            # 만든 숫자가 타겟과 일치하는지 확인하고
            # 일치하면 방법 수 +1
            if check_num == target:
                answer += 1
            return answer
            # 만든 숫자가 타겟과 일치하지 않아도 리턴
            return
        # 아직 덜 선택했다면 operator를 선택하기
        elif idx < N:
            # 모든 operator 에 대해서
            for operator in operators:
                # 만약 + 를 선택했을 경우
                if operator == '+':
                    # idx+1 번째 operator 를 선택하러 가기, 만든 숫자에 이번 숫자 더해주기
                    solve(idx+1, check_num + numbers[idx])
                # 만약 - 를 선택했을 경우
                if operator == '-':
                    # idx+1 번째 operator 를 선택하러 가기, 만든 숫자에 이번 숫자 빼주기
                    solve(idx+1, check_num - numbers[idx])


    # 사용할 변수들 선언
    operators = ['+','-'] # operator 를 나열
    N = len(numbers) # 전체 사용할 총 숫자의 개수
    answer = 0 # 전체 방법의 수 구하는 변수
    # 타겟 넘버를 만드는 방법의 수 return
    solve(0, 0) # idx, check_num
    return answer