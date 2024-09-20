def solution(commands:list[list[str]])->str:
    current_time = int(commands[-1][2]) + 1
    result = []
    for i in range(len(commands) - 1, -1, -1):
        command = commands[i]
        time = int(command[2])
        if current_time <= time:continue
        else:current_time = time
        if command[0] == "undo":
            current_time -= int(command[1])
        elif command[0] == "type":
            result.append(command[1])
    return ''.join(result[::-1])

n = int(input())
commands = list()
for _ in range(n):
    command = input().split()
    commands.append(command)
ans = solution(commands)
print(ans)