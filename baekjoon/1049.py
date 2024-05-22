N,M = map(int,input().split())
minValue = 1000
multiple = N // 6
mod = N % 6
minPackageValue = 1000
minSingleValue = 1000

for _ in range(M):
    package,single = map(int,input().split())
    minPackageValue = min(minPackageValue,package)
    minSingleValue = min(minSingleValue,single)
ans = min(minPackageValue*multiple + minSingleValue * mod, minPackageValue*(multiple+1), minSingleValue*N)
print(ans)