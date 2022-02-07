target = input()
upper_target = target.upper()
solve = {}
maximum = 0
for i in upper_target:
    if solve.get(i) == None:
        solve.update({i:1})
    else:
        solve[i] += 1

for j in solve.items():
    if maximum < j[1]:
        maximum = j[1]
        maximum_key = j[0]
    elif maximum == j[1]:
        maximum_key += j[0]

if len(maximum_key) > 1:
    print('?')
else:
    print(maximum_key)