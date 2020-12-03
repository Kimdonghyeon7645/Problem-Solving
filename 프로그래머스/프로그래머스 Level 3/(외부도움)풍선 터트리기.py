def solution(a):
    answer = 2
    lists = [[] for _ in range(2)]
    left, right = 1000000001, 1000000001
    print("왼쪽 배열")
    for l in a:
        left = (l if left > l else left)
        lists[0].append(left)
        print("헤이", len(lists[0])-1, left)
    print("오른쪽 배열")
    for r in a[::-1]:
        right = (r if right > r else right)
        lists[1].append(right)
        print("헤이", len(lists[1])-1, right)
    for i, target in enumerate(a[1:-1]):
        i += 1
        print(lists[0][i-1], target, lists[1][len(a)-i-2])
        if lists[0][i-1] > target or target < lists[1][len(a)-i-2]:
            answer += 1
    return answer


"""
너무 오래 시간을 써서 결국 정보의 바다 인터넷을 이용했다...
맨 앞, 맨 뒷 풍선은 어떻게든지 남길 수 있었다. 
(1. 최대값 살리기 찬스를 쓰지 않고 한쪽 방향의 최소값 1개를 남긴다. 2. 찬스를 쓰든 말든 해서 남은 두개중 살릴 얘를 살린다.)
가운데 풍선은 양쪽 방향마다 각각 
(1. 최대값 살리기 찬스를 쓰지 않고, 양쪽 방향에서 각각 최소값 1개를 남긴다. 2. 2개중에 하나보단 적으면 나머지 하나는 찬스를 쓰든 말든 해서 살린다.) 
"""
# 테스트 코드
print(solution([9, -1, -5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
