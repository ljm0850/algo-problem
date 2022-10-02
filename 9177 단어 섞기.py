import sys
def solve(str1:str,str2:str,target:str)->bool:
    stack = [(0,0,0)]
    check = {}
    while stack:
        idx_str1,idx_str2,idx_target = stack.pop()
        if idx_target == len(target):
            return True
        if idx_str1 < len(str1) and target[idx_target] == str1[idx_str1] and not check.get((idx_str1+1,idx_str2)):
            stack.append((idx_str1+1,idx_str2,idx_target+1))
            check[(idx_str1+1,idx_str2)] = True
        if idx_str2 < len(str2) and target[idx_target] == str2[idx_str2] and not check.get((idx_str1,idx_str2+1)):
            stack.append((idx_str1,idx_str2+1,idx_target+1))
            check[(idx_str1, idx_str2+1)] = True
    return False

n = int(sys.stdin.readline())
for tc in range(1,n+1):
    first,second,target = sys.stdin.readline().split()
    ans = solve(first,second,target)
    if ans:
        print(f'Data set {tc}: yes')
    else:
        print(f'Data set {tc}: no')