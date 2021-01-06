def solution(n, works):
    """
    알고리즘 문제 설명이 어렵다.. 풀어 말하자면,
    :param works:에 처리할 일의 소요시간이 숫자 배열로 저장되며,
    :param n:에 처리할 수 있는 시간이 숫자로 저장된다.
    :return:으론, 처리할 일 각각을 제곱한 값을 모두 더한 값의 최소값을 출력하면 된다.
    그니까 works 숫자 배열에서 n개 만큼을 빼서, 남은 works 요소들의 제곱을 모두 더한 값의 최소값이 나오면 된다.
    """

    # way 1. 간단하게 풀었지만, 효율성(시간복잡도)에서 당연하게도 걸린다.
    for _ in range(n):
        works[works.index(max(works))] -= 1
    return sum(i ** 2 for i in works if i > -1)


# 테스트 코드
print(solution(4, [4, 3, 3]))

