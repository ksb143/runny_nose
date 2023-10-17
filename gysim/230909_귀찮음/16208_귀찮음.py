n = int(input())
nums = list(map(int, input().split()))

# 길이 a1+a2+a3+...+an 인 쇠막대를 a1, a2, ..., an으로 자르고싶다
# 길이 x+y인 막대를 자르면 길이의 곱 xy의 비용이 든다

# a1, a2, a3, a4를 잘라보자
# 1. a1*(a2+a3+a4) + a2*(a3+a4) + a3*a4
# 2. (a1+a2)*(a3+a4) + a1*a2 + a3*a4
# 어떻게 자르든 결과는 같다 -> 순서상관없이 막 자르면됨

# 막대의 총 길이 구하기
total = 0
for i in range(n):
    total += nums[i]

ans = 0
for j in range(n-1):    # 0번부터 N-2번째 숫자까지
    # 자기자신*(남은 막대길이 - 자기자신) 더해주기
    ans += nums[j]*(total-nums[j])  
    total -= nums[j]    # 남은 막대길이는 자기 자신을 뺀 값

print(ans)
