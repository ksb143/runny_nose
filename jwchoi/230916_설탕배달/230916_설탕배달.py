N = int(input())
# min_ans = 1666
ans0= -1
if N%5 ==0:                     # 5로 나눠떨어지면, 그냥 5의 몫이 답임 ex) 15
    ans0 = N//5
else:                           # But, 5로 안나눠떨어지면..? 좀더 복잡해짐. ex) 11, 17, 18 ==> 3,5,4
    cnt = 0
    a = N//5 # 2, 3, 3
    b = N//3 # 3, 5, 6
    l= []
    for x in range(a+1):
        for y in range(b+1):
            cnt += 1
            # print(cnt)
            if cnt < (a+1)*(b+1) and (5*x) + (3*y) == N:
                l.append(x+y)
            elif cnt == (a+1)*(b+1):
                if l != []:
                    if (5*x) + (3*y) == N:
                        l.append(x + y)
                        ans0 = min(l)
                    else:
                        ans0 = min(l)
                elif l ==[]:
                    if (5*x) + (3*y) == N:
                        ans0 = x+y
print(ans0)