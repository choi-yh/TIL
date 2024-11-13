import sys

n = int(sys.stdin.readline())
s = set()
for _ in range(n):
    command = sys.stdin.readline().rstrip().split(" ")
    if command[0] == "add":
        s.add(command[1])
    elif command[0] == "remove":
        s.discard(command[1])
    elif command[0] == "check":
        if command[1] in s:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        if command[1] in s:
            s.discard(command[1])
        else:
            s.add(command[1])
    elif command[0] == "all":
        s = set(map(str, range(1, 21)))
    elif command[0] == "empty":
        s = set()
