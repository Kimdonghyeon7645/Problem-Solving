def solution(heights):
    answer = [0] * len(heights)
    for i, n in enumerate(heights):
        for j in range(i-1, -1, -1):
            if heights[j] > n:
                answer[i] = j + 1
                break
    return answer


print(solution([6,9,5,7,4]))
# 이중 for 문으로 효율이 별로여서 점수도 낮게나와 시무륵 했는데, 추천을 가장많이 받은 풀이와 알고리즘이 똑같에서 기분이 다시 좋아졌다!
