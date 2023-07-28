def main():
    n = int(input())
    min_days = 1
    logs = [[int(s) for s in input().split(':')] for x in range(n)]

    for i in range(len(logs) -1):
        if logs[i][0] > logs[i + 1][0]:
            min_days += 1
            continue
        elif logs[i][0] == logs[i + 1][0]:
            if logs[i][1] > logs[i + 1][1]:
                min_days += 1
                continue
            elif logs[i][1] == logs[i + 1][1]:
                if logs[i][2] > logs[i + 1][2]:
                    min_days += 1
                    continue
                elif logs[i][2] == logs[i + 1][2]:
                    min_days += 1

    print(min_days)


if __name__ == '__main__':
    main()