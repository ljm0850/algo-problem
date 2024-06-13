# R I N G S
# 문자열의 길이는 20
# 돌다리의 길이는 100

# 차라리 돌다리idx 기준?, 값은 문자열 IDX
#  R,G,S ...
# [2,1,2,...]
# GRGGNS
# [1,2,1,...]


def solution(sentence:str,bridge:list[str])->int:
    # 각 알파벳 idx들 기록
    alphaTotal = {"R":[],"I":[],"N":[],"G":[],"S":[]}
    S = len(sentence)
    for i in range(S):
        alpha = sentence[i]
        alphaTotal[alpha].append(i)
    
    B = len(bridge)
    L = len(bridge[0])
    check = [[0]*S for _ in range(B)]
    for idx in range(L):    # 다리idx 
        temp = list()
        for i in range(B):  # 어떤 다리인지, 천사 or 악마 다리
            alpha = bridge[i][idx]
            for num in alphaTotal[alpha]:
                if num == 0:
                    temp.append((i,num,1))
                else:
                    value = 0
                    for v in range(B):
                        if v == i:continue
                        value += check[v][num-1]
                    temp.append((i,num,value))
        for r,c,cnt in temp:
            check[r][c] += cnt
    ansValue = 0
    for i in range(B):
        ansValue += check[i][S-1]
    return ansValue
sentence = input()
devil = input()
angle = input()
ans = solution(sentence,[devil,angle])
print(ans)