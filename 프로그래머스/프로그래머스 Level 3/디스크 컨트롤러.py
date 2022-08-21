def solution(jobs):
    jobs.sort(key=lambda x: x[0])
    print(jobs)
    job_rdy = []
    job_end = []
    t = 0
    left_t = 0
    for i in range(len(jobs)):
        if t < jobs[i][0]:

        if left_t < jobs[i][0]:
            t += left_t
            left_t = 0
        else:
            t += jobs[i][1]

    return sum(job_end) // len(job_end)


if __name__ == '__main__':
    print(solution([[0, 3], [1, 9], [2, 6]]))
