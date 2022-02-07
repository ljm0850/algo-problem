target = input()

cnt = 1
if target.strip() == '':
    cnt = 0
for i in target.strip():
    if i == ' ':
        cnt += 1
    
print(cnt)