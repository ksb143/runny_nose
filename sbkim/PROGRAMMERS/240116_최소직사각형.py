# 명함 지갑을 만드는 회사에서 지갑의 크기를 정하려고 합니다.
# 다양한 모양과 크기의 명함들을 모두 수납할 수 있으면서, 작아서 들고 다니기 편한 지갑을 만들어야 합니다.
# 이러한 요건을 만족하는 지갑을 만들기 위해 디자인팀은 모든 명함의 가로 길이와 세로 길이를 조사했습니다.
#
# 모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어집니다.
# 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# sizes의 길이는 1 이상 10,000 이하입니다.
    # sizes의 원소는 [w, h] 형식입니다.
    # w는 명함의 가로 길이를 나타냅니다.
    # h는 명함의 세로 길이를 나타냅니다.
    # w와 h는 1 이상 1,000 이하인 자연수입니다.


def solution(sizes):
    width = []
    height = []
    for w, h in sizes:
        # 큰 게 width에 들어가도록 하기
        if w >= h:
            width.append(w)
            height.append(h)
        else:
            width.append(h)
            height.append(w)
    # 나눈 것 중에 max 값을 찾기
    answer = max(width) * max(height)
    return answer