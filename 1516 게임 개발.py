import sys
input = sys.stdin.readline

def find_max_buid_time(arr:list[int])->int:
    value = 0
    for i in arr:
        value = max(value,build_time[i])
    return value

N = int(input())
spending_time = [0]*(N+1)
graph = [[] for _ in range(N+1)]
r_graph = [[] for _ in range(N+1)]
condition = [0]*(N+1)

for idx in range(1,N+1):
    value = list(map(int,input().split()))
    spending_time[idx] = value[0]
    condition[idx] = len(value) -2
    for i in range(1,len(value)-1):
        graph[value[i]].append(idx)
        r_graph[idx].append(value[i])

build_time = [0]*(N+1)
total = set([i for i in range(1,N+1)])

build_complete = list()
while len(total) != 0:
    # 현재 지을수 있는 건물들 짓기
    for idx in total:
        if condition[idx] == 0:
            build_complete.append(idx)
            build_time[idx] += spending_time[idx]

    # 조건 처리된 내역 모음
    for idx in build_complete:
        for n_idx in graph[idx]:
            condition[n_idx] -= 1
            if condition[n_idx] == 0:
                build_time[n_idx] += find_max_buid_time(r_graph[n_idx])
        total.remove(idx)
    build_complete.clear()

for i in range(1,N+1):
    print(build_time[i])