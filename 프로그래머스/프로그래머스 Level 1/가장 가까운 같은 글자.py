def solution(s):
    answer = []
    latest = {}
    for i in range(len(s)):
        answer.append((i-latest[s[i]]) if s[i] in latest else -1)
        latest[s[i]]=i
    return answer