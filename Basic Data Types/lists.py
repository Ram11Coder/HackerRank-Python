if __name__ == '__main__':
    N = int(input())
    li = []
    for x in range(0, N):
        action, *line = input().split()
        op = list(map(int, line))
        if action == 'insert':
            li.insert(op[0], op[1])
        elif action == 'remove':
            if not li.index(op[0]) is None:
                li.remove(op[0])
        elif action == 'append':
            li.append(op[0])
        elif action == 'pop':
            li.pop()
        elif action == 'sort':
            li.sort()
        elif action == 'print':
            print(li)
        elif action == 'reverse':
            li.reverse()
