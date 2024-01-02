N = int(input())
record = [i for i in range(N+1)]
for i in range(7,N+1):
    record[i] = max(record[i-4]*3, record[i-5]*4)
print(record[N])