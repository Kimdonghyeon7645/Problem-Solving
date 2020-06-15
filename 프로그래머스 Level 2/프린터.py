def solution(priorities, location):
    # lmax = len(priorities)
    # if location:
    #     location -= 1
    # while True:
    #     print(priorities)
    #     top = priorities.pop(0)
    #     if priorities[0] != max(priorities):
    #         if location == 0:   # 1이 이 구문에 들어가는 오류
    #             location += len(priorities)
    #         priorities.append(top)
    #     elif location == 0:
    #         break
    #     location -= 1
    # return lmax - len(priorities)
    m = len(priorities)                     
    n = priorities[location]                
    i = priorities.index(max(priorities))   
    print(i, priorities[i])                 
    while True:                             
        i += 1                              
        if i >= len(priorities):            
            i = 0                           
        if priorities[i] == max(priorities):
            if priorities.pop(i) == n:      
                break                       
    return m - len(priorities)              


print(solution([2, 1, 3, 2], 2))
