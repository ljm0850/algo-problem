def solve(target:str)->list:
    arr = []
    for idx in range(len(target)):
        arr.append(target[idx:])
    arr.sort()
    return arr
S = input()
answer=solve(S)
for ans in answer:
    print(ans)