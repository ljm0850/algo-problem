from collections import Counter
def isSimilar(word1:str,word2:str,set_word2:set[str])->int:
  if abs(len(word1) - len(word2)) >= 2:
    return 0
  count1 = Counter(word1)
  count2 = Counter(word2)
  gap = 0
  for alpha in (set(word1)|set_word2):
    gap += abs(count1[alpha]-count2[alpha])
  if gap <= 2:
    return 1
  return 0

def solution(N:int,target:str,words:list[str])->int:
  cnt = 0
  set_target = set(target)
  for word in words:
    cnt += isSimilar(word,target,set_target)
  return cnt
# 입력
N = int(input())
target = input()
words = [input() for _ in range(N-1)]
ans = solution(N,target,words)
print(ans)