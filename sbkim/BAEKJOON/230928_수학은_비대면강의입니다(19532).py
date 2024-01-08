a, b, c, d, e, f = map(int, input().split())

# 공배수 찾기
cm_x = a * d
# 공배수가 되기 위해 곱해야하는 수
if a != 0 and d != 0:
    a_multi = cm_x // a
    d_multi = cm_x // d

    y1, result1 = b * a_multi, c * a_multi
    y2, result2 = e * d_multi, f * d_multi

    y = (result1 - result2) // (y1 - y2)
    x = (c - y * b) // a
# 0일 때 고려
elif a == 0:
    y = c // b
    x = (f - y * e) // d
else:
    y = f // e
    x = (c - y * b) // a

print(x, y)