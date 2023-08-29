import sys
input = sys.stdin.readline
N = int(input())
E = int(input())
total = []
for _ in range(E):
    K,*people = map(int,input().split())
    people = set(people)
    if 1 in people:
        total.append(people)
    else:
        for song in total:
            for person in people:
                if person in song:
                    song.update(people)
                    break
ans =  set(i for i in range(1,N+1))
for song in total:
    ans = ans & song
ans = sorted(list(ans))
for v in ans:
    print(v)