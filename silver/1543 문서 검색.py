document = input()
target = input()
l1 = len(document)
l2 = len(target)
i,cnt = 0,0
while i < l1:
    if document[i:i+l2] == target:
        cnt += 1
        i += l2
    else:
        i += 1
print(cnt)