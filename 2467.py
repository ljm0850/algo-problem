N= int(input())
solution = list(map(int,input().split()))
solution.sort()
s=0
e=N-1

best_ss=abs(solution[0]+solution[N-1])
best_s,best_e=solution[s],solution[e]
while s<e:
    ss=solution[s]+solution[e]
    if  abs(ss) <= best_ss:
        best_ss = abs(ss)
        best_s = solution[s]
        best_e = solution[e]
    
    if ss > 0:
        e -=1
    elif ss < 0 :
        s +=1
    else:
        break
print(best_s,best_e)