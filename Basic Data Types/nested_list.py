if __name__ == '__main__':
    records = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.update({name: score})
result = []
second_max = sorted(set(records.values()))[1]
for k in sorted(records.keys()):
    if records.get(k) == second_max:
        print(k)
