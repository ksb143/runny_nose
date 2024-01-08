N = int(input())

word_set = set()

for _ in range(N):
    word = input()
    word = (len(word), word)
    word_set.add(word)

word_list = list(word_set)
word_list.sort(key=lambda x: (x[0], x[1]))

for l, w in word_list:
    print(w)
