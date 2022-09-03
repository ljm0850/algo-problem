import sys
def solve(k):
    global ans
    if k < 5:
        return
    elif k == 26:
        ans = N
        return
    recur(1,0,k-5)

def recur(i,cnt,k):
    global ans
    if cnt == k:
        reading_word = 0
        for word in words:
            for alphabet in word:
                if not alpha[ord(alphabet)-97] :
                    break
            else:
                reading_word += 1
        if ans < reading_word:
            ans = reading_word
        return

    for index in range(i,26):
        if alpha[index]:
            continue
        alpha[index] = True
        recur(index+1,cnt+1,k)
        alpha[index] = False

N,K = map(int,sys.stdin.readline().split())
words = [sys.stdin.readline()[4:-4]for _ in range(N)]
# ord('a') = 97
alpha = [False]*26
alpha[0],alpha[2],alpha[8],alpha[13],alpha[19] = True,True,True,True,True
ans = 0
solve(K)
print(ans)