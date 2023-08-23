def solution(today, terms, privacies):
    date1ym = int(today[:4])*12+int(today[5:7])
    date1d = int(today[8:])
    tdic = dict((t.split()[0], int(t.split()[1])) for t in terms)
    r = []
    for i,p in enumerate(privacies):
        date2,tcd=p.split()
        date2ym = int(date2[:4])*12+int(date2[5:7])+tdic[tcd]
        if date1ym > date2ym or (date1ym == date2ym and date1d > int(date2[8:])-1):
            r.append(i+1)
    return r