N = int(input())
customers = list(map(int,input().split()))
pc = [False]*101
ans = 0
for customer in customers:
    if not pc[customer]:pc[customer] = True
    else:ans+=1
print(ans)