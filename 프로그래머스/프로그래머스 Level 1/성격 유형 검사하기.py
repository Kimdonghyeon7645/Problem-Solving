def solution(survey, choices):
    answer = dict().fromkeys("RTCFJMAN", 0)
    for i in range(len(choices)):
        answer[survey[i][choices[i] // 4]] += abs(choices[i] - 4)
    return "".join(a if answer[a] >= answer[b] else b for a, b in ["RT", "CF", "JM", "AN"])


if __name__ == "__main__":
    print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))    # TCMA
    print(solution(["TR", "RT", "TR"], [7, 1, 3]))    # RCJA

