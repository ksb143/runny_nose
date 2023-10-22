def pick(min_c, min_v, cnt_t, picked, idx):



pick_num, total_num = map(int, input().split())
alphabets = list(input().split())
vwls_tot = ['a','e','i','o','u']
consonants = list(set(alphabets) - set(vwls_tot))
vowels = list(set(alphabets)-set(consonants))
c = len(consonants)
v = len(vowels)
#min_c = 2 최소 2개의 자음 선택 필수
#min_v = 1 최소 1개의 모음 선택 필수
#cnt_t = 0 cnt_t = pick_num 일 경우 그만 뽑기

picked_lst = []
pick(2,1,0,'',0)
print(picked_lst)