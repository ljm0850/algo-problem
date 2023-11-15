N = int(input())
flag = False
record = set()
for _ in range(N):
    a,b = input().split()
    if record:
        if a in record or b in record:
            record.add(a)
            record.add(b)
    else:
        if a == 'ChongChong' or b == 'ChongChong':
            record.add(a)
            record.add(b)
print(len(record))