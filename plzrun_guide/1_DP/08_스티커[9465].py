# 여덟번째 DP, dp적용하는 문제인 줄 몰랐지만 dp를 적용하며 해결
"""
예전같으면 주먹구구로 접근할 수 있지만 이제는 DP로 바텀-업(하향식)을 적용한다.
2행 n열 이면, 열이 1부터 n까지 경우를 메모이제이션 하면서 최댓값을 구할 수 있도록 점화식을 세우고 코드로 구현했더니 해결됬다.
"""
for _ in range(int(input())):
    n = int(input())
    d = [[int(i) for i in t.split()] for t in [input(), input()]]
    for i in range(1, n):
        for j in range(2):
            d[j][i] = max(d[j][i-1], d[0 if j else 1][i-1]+d[j][i])
    print(max(d[0][-1], d[1][-1]))


"""
### 처음 예상한 점화식
d[i][j] = 
    (if j == 0) max(d[i-1][j] , d[i-3][j]+d[i][j] , d[i-1][1]+d[i][j])
    (if j == 1) max(d[i-1][j] , d[i-3][j]+d[i][j] , d[i-1][0]+d[i][j])
생각해보니, d[i-3][j]+d[i][j] 는 차피 d[i-1][1]+d[i][j] 에서 이미 비교해서 d[i-1][1]+d[i][j]에 이미 큰 값이 들어있기에 제외
### 최종 점화식
d[i][j] = 
    (if j == 0) max(d[i-1][j] , d[i-1][1]+d[i][j])
    (if j == 1) max(d[i-1][j] , d[i-1][0]+d[i][j])

# case 1
99 2 3 98
5 1 4 6
"""