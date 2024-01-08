from collections import defaultdict

def solution(participant, completion):
    candidates = defaultdict(int)
    for runner in participant:
        candidates[runner] += 1
    for runner in completion:
        candidates[runner] -= 1
    for answer in candidates:
        if candidates[answer] != 0:
            return answer