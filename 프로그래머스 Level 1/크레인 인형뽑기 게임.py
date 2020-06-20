def solution(board, moves):
    box = []
    out = [0]
    rm = 0
    for i in zip(*tuple(board[i] for i in range(len(board)))):
        box.append(list(filter(lambda x: x, i)) + [0])
    for i in moves:
        temp = box[i-1].pop(0) if box[i-1][0] else -1
        if temp == out[-1]:
            del out[-1]
            rm += 2
        elif temp != -1:
            out.append(temp)
    return rm


# 아래는 테스트 코드
print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
