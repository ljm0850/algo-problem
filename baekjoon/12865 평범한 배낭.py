N,K = map(int,input().split())
backpack = [0]*(K+1)
for _ in range(N):
    W,V = map(int,input().split())
    for i in range(len(backpack))[::-1]:
        if backpack[i] and i + W <= K:
            backpack[i+W] = max(backpack[i+W],backpack[i]+V)
    if W <= K:
        backpack[W] = max(backpack[W],V)
print(max(backpack))