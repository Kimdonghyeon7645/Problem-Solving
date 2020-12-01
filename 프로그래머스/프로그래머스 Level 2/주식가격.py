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


def solution_b(p):      # 나의 기존 로직보다 무려 4배나 더 효율이 좋다. 한번 분석해보자
    ans = [0] * len(p)
    stack = [0]
    for i in range(1, len(p)):      # 두번째 원소 인덱스부터 마지막 원소 인덱스까지
        if p[i] < p[stack[-1]]:     # == 혹시 기존의 스텍중에서 하나라도 가격이 떨어진 게 있는가?
            # 지금 빼온 원소가 스텍의 마지막 원소보다 작은지 본다. (스텍에는 원소가 큰 게 점점 쌓이지 작은 게 쌓이지 못한다.)
            # 그래서, 스텍은 오름차순 정렬이기에, 모든 원소와 비교할 필요 없이 마지막(가장 큰) 원소랑 비교해도 된다.
            # 스텍의 가장 큰 놈이랑 비교했을 때도 지금 빼온 것이 크면, 스텍의 나머지 놈들도 지금 빼온 것보다 작을 것이기 때문이다.
            for j in stack[::-1]:   # 스텍을 꺼꾸로 순회해서, (내림차순으로) 가격이 떻어진 것들을 구한다
                if p[i] < p[j]:     # 실제 스텍의 원소가 지금 빼온 원소랑 비교했을 때 가격이 떨어졌는가?
                    ans[j] = i-j    # 그럼, 가격이 떨어진 것을 저장한다.
                    stack.remove(j)     # 가격이 떨어진 값을 저장했으니, 스텍에서는 생각하지 않는다.
                else:
                    # 비교한 원소가, 지금 빼온 원소보다 작기 시작했다면, 지금 이건 내림차순(stack[::-1])이기에,
                    # 나머지 스텍의 원소들도 비교한 원소보다 작으니, 지금 빼온 원소랑도 반드시 작을 것이다.
                    # 그러면 차피 더이상 계산할 필요가 없으니 break 로 빠져나온다.
                    break
        stack.append(i)
    for i in range(0, len(stack)-1):
        # 끝까지 반복문 돌았는데, 남아있는 놈들은, 가격 변화가 끝까지 없는 놈들이다.
        # 그러면 곧, 가격 변화는 (총 리스트 길이) - ((인덱스 길이) + 1) 초가 되는 것이다.
        ans[stack[i]] = len(p) - stack[i] - 1
    return ans


# 리스트 슬라이싱 때문에 시간초과 문제가 생겼는데, 그래서 c 스타일 코드로 작성했다.
# 리스트 슬라이싱은 O(k) (k는 잘라낸 리스트 크기) 의 시간복잡도를 가지는 점 참고하자.
print(solution([1, 2, 3, 2, 3]))
print(solution_b([1, 2, 3, 2, 3]))
