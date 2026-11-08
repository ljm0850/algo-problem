def solution(name, yearning, photo):
    matchingData = {}
    answer = []
    for i in range(len(name)):
        matchingData[name[i]] = yearning[i]
    for p in photo:
        v = 0
        for n in p:
            
            v += matchingData.get(n,0)
        answer.append(v)
    return answer