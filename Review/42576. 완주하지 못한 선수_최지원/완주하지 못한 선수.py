from collections import Counter

def solution(participant, completion):
    cp,cc = Counter(participant),Counter(completion)
    result = cp -cc

    return list(result.keys())[0]