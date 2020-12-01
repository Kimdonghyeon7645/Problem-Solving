def solution(n, words):
    word_set = {words[0]}
    for i in range(1, len(words)):
        if words[i] in word_set or words[i-1][-1] != words[i][0]:
            return [(i % n)+1, (i // n)+1]
        else:
            word_set.add(words[i])
    return [0, 0]


# 테스트 코드
print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
