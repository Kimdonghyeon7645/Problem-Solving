def solution(prices):
    answer = []
    for i, n in enumerate(prices):
        rt = 0
        for j in range(i+1, len(prices)):
            if prices[j] < n or j+1 == len(prices):
                rt = j - i
                break
        answer.append(rt)
    return answer


# 리스트 슬라이싱 때문에 시간초과 문제가 생겼는데, 그래서 c 스타일 코드로 작성했다.
# 리스트 슬라이싱은 O(k) (k는 잘라낸 리스트 크기) 의 시간복잡도를 가지는 점 참고하자.
print(solution([1, 2, 3, 2, 3]))