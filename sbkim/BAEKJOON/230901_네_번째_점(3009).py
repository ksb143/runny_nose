row_dic = {}
col_dic = {}

# 각 좌표의 row, col 값 찾기
for _ in range(3):
    r, c = map(int,input().split())
    try:
        row_dic[r] += 1
    except:
        row_dic[r] = 1
    try:
        col_dic[c] += 1
    except:
        col_dic[c] = 1

# row 값 중 부족한 것이 네 번째 점의 row 값
for r in row_dic:
    if row_dic[r] == 1:
        last_r = r

# col 값 중 부족한 것이 네 번째 점의 col 값
for c in col_dic:
    if col_dic[c] == 1:
        last_c = c

print(last_r, last_c)
