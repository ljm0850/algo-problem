def solution(Target:str):
    if Target == 'P' or Target == 'PPAP':
        return True
    ls = []
    ppap = ['P','P','A','P']
    for t in Target:
        ls.append(t)
        if ls[-4:] == ppap:
            for _ in range(3):
                ls.pop()
    if ls == ['P'] or ls == ppap:
        return True
    return False

Target = input()
ans = solution(Target)
if ans:
    print('PPAP')
else:
    print('NP')