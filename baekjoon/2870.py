def findNum(target:str)->list[int]:
  i = 0
  value = list()
  while i < len(target):
    alpha = target[i]
    i += 1
    if alpha.isdigit():
      temp = alpha
      while i < len(target):
        if target[i].isdigit():
            temp += target[i]
            i += 1
        else:
          break
      value.append(int(temp))
  return value

N = int(input())
ls = list()
for _ in range(N):
  paper = input()
  v = findNum(paper)
  ls += v
ls.sort()
for num in ls:
  print(num)
