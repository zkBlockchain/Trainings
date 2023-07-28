def main():
    n = int(input())
    array = [[input(), input()] for x in range(n)]

    for swap_1, swap_2 in array:
        if len(swap_1) != len(swap_2):
            print('NO')
            continue

        swap_1_dicts = {}
        swap_2_dicts = {}
        for i in range(len(swap_1)):
            if swap_1[i] in swap_1_dicts:
                if swap_2[i] != swap_1_dicts[swap_1[i]]:
                    print('NO')
                    break
                else:
                    continue
            else:
                swap_1_dicts[swap_1[i]] = swap_2[i]

            if swap_2[i] in swap_2_dicts:
                if swap_1[i] != swap_2_dicts[swap_2[i]]:
                    print('NO')
                    break
                else:
                    continue
            else:
                swap_2_dicts[swap_2[i]] = swap_1[i]
        else:
            print('YES')


if __name__ == '__main__':
    main()