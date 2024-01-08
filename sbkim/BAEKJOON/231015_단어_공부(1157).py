word = input()

word_num = {}

for w in word:
    w = w.upper()
    try:
        word_num[w] += 1
    except:
        word_num[w] = 1


num_lst = []
max_num = 0

for key, value in word_num.items():
    num_lst.append(value)
    if max_num < value:
        max_num = value
        max_word = key

if num_lst.count(max_num) == 1:
    print(max_word)
else:
    print('?')