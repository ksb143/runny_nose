from collections import Counter
# Counter class를 활용하여 계산 효율성을 높이었음
# https://docs.python.org/ko/3/library/collections.html#collections.Counter : 공식문서
def solution(participant, completion):
    cp,cc = Counter(participant),Counter(completion) # Counter class를 통해 참가자를 cp, 완주자를 cc로 재정의
    result = cp -cc # Counter 객체를 subtract(빼기)하여 요소 합계를 result로 구함.

    return list(result.keys())[0] # Counter 객체의 key 들을 반환하는 keys() 메써드를 활용하여 완주자 수와 차이나는 참가자를 골라내 반환함.

# # 아래는 이해를 위한 예시
# from collections import Counter

# # Counter 객체 생성
# c = Counter(["apple", "banana", "apple", "cherry", "banana"])
# print(c)
# # 키를 가져오기
# keys = c.keys()
# print(keys)
# # 결과 출력
# print(list(keys))
