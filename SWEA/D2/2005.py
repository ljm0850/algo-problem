T = int(input())

def tri(x) :
    if x == 1:
        return [1]
    elif x == 2:
        return [1,1]
    else:
        solve =[1]
        for i in range(1,x-1):
            solve.append(tri(x-1)[i]+tri(x-1)[i-1])
        solve.append(1)        
        
        return solve

for i in range (T):
    N = int(input())
    print(f'#{i+1}')
    for j in range(1,N+1):        
        print(' '.join(map(str,tri(j))))