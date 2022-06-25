import sys
def make_tree():
    for _ in range(V):
        info = list(map(int, sys.stdin.readline().split()))
        p = info[0]
        i = 1
        end = len(info)//2
        while i < end:
            if info[2 * i - 1] == -1:
                break
            ch = info[2*i-1]
            v = info[2*i]
            tree[p][ch] = v
            i += 1

def find_point(s):
    stack = [(s,0)]
    point,long = 0,0
    visited = [0]*(V+1)
    visited[s] = 1
    while stack:
        now,length = stack.pop()
        for next,next_length in tree[now].items():
            if not visited[next]:
                visited[next] = 1
                stack.append((next,length+next_length))
            else:
                if long < length:
                    point = now
                    long = length
    return point,long

V = int(input())
tree = [{} for _ in range(V+1)]
make_tree()
p1 = find_point(1)[0]
p2 = find_point(p1)
print(p2[1])