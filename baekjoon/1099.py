def sortedWordDict(words:list[str])->dict:
    dictionary = dict()
    for word in words:
        sortedWord = ''.join(sorted(word))
        dictionary[sortedWord] = dictionary.get(sortedWord,[]) + [word]
    return dictionary

def gapCheck(word1:str,word2:str)->int:
    value = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]: value += 1
    return value

def recur(sentence:str,value:int):
    global check,wordDict,maxValue,record
    if len(sentence) == 0:
        return value

    S = len(sentence)
    minValue = maxValue
    for i in range(1,S+1):
        word = sentence[:i]
            
        if not word in record:
            sortedWord = ''.join(sorted(word))
            if sortedWord in wordDict:
                minGap = maxValue
                for originWord in wordDict[sortedWord]:
                    gap = gapCheck(word,originWord)
                    minGap = min(minGap,gap)
                record[word] = minGap
            else:
                record[word] = -1
                continue
        
        if record[word] == -1:
            continue
        
        remianSentence = sentence[i:]
        nextValue = value + record[word]
        if check[len(remianSentence)] > nextValue:
            check[len(remianSentence)] = nextValue
            v = recur(remianSentence,nextValue)
            minValue = min(minValue,v)
    return minValue

sentence = input()
N = int(input())
words = [input() for _ in range(N)]
maxValue = 51
check = [maxValue]*(len(sentence)+1)
record = dict()
wordDict = sortedWordDict(words)
ans = recur(sentence,0)
if ans != maxValue : print(ans)
else: print(-1)