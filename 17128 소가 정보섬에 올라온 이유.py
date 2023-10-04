def recording(cnt:int,N:int,caws:list[int])->list[int]:
    value = [0]*N
    v = 1
    for i in range(cnt):
        v *= caws[i]
    value[0] = v
    for i in range(1,N):
        v //= caws[i-1]
        v *= caws[(i+3)%N]
        value[i] = v
    return value

def solution(cnt:int,trick:list[int],record:list[int])->None:
    total = sum(record)

    for i in trick:
        i -= 1
        for j in range(cnt):
            k = i-j
            record[k] = - record[k]
            total += 2*record[k]
        print(total)

N,Q = map(int,input().split())
cnt = 4
caws = list(map(int,input().split()))
trick = list(map(int,input().split()))
record = recording(cnt,N,caws)
solution(cnt,trick,record)