def make_cypher(length,index,ans):
    if length == L:
        test1,test2=0,0
        for t in ans:
            if t in ['a','e','i','o','u']:
                test1 +=1
            else:
                test2 +=1
            if test1 >=1 and test2 >=2:
                print(ans)
                break
        return
    for i in range(index+1,C):
        make_cypher(length+1,i,ans+alpha[i])

L,C = map(int,input().split())
alpha = sorted(input().split())
make_cypher(0,-1,'')
