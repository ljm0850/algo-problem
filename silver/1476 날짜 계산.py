def solve(e:int,s:int,m:int)->int:
    year = 1
    while True:
        if e==E and s == S and m == M:
            return year
        year +=1
        e = (e)%15+1
        s = (s)%28+1
        m = (m)%19+1

E,S,M = map(int,input().split())
ans=solve(1,1,1)
print(ans)