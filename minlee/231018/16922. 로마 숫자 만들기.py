# 같은 거 뽑을 수 있게 해야하고, 이게 바로 중복조합..?!
# 쓸 수 있는 문자 다 넣어놓고 N개 뽑아보기

def johap(idx, num, count):
    # 인덱스를 증가시켜주면서 넣을 요소를 변경시켜주기
    # num은 요소들 합쳐지면서 만들어지는 값
    # count는 몇 개의 요소가 지금까지 모였는지
    # (N개까지만 담을 수 있음)
    if count == N:
        if num not in answer:
            answer.add(num)
        return
    if idx >= len(roma):
        # 같아야하는 이유는 밑에 roma[idx] 했을 때
        # 인덱스 에러나는 걸 방지하기 위해
        return

    johap(idx+1, num+roma[idx], count+1)
    # 인덱스 증가, 요소 더하기(한 요소가 만들어질 수 있는 조합이 다 되어서 다음 요소로 넘어갈 수 있도록)
    johap(idx, num + roma[idx], count + 1)
    # 인덱스 그대로, 요소 더하기(같은 요소 차례일 때 들어갈 수 있도록)
    johap(idx+1, num, count)
    # 다음 요소로 넘어가지만 아무것도 더하지 않은 상태

N = int(input())
roma = [1, 5, 10, 50]

# 답 넣을 빈 세트(리스트보다 시간이 더 줄어들어요!)
# 들어오는 순서를 찾는 문제면 set로는 힘들수도..!
answer = set()

johap(0, 0, 0)

print(len(answer))