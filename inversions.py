def merge(array):
    array_len = len(array)
    if not array_len or array_len == 1:
        return array, 0
    if array_len == 2:
        if array[0] > array[1]:
            return [array[1], array[0]], 1
        else:
            return array, 0
    
    left, left_inv = merge(array[:array_len // 2])
    right, right_inv = merge(array[array_len // 2:])
    left_len, right_len = len(left), len(right)
    
    n, m = 0, 0
    results = []
    inversions = left_inv + right_inv
    while n < left_len and m < right_len:
        if left[n] > right[m]:
            results.append(right[m])
            inversions += left_len - n
            m += 1
        else:
            results.append(left[n])
            n += 1
    
    results.extend(left[n:])
    results.extend(right[m:])
    return results, inversions


def main():
    n = int(input())
    array = [int(x) for x in input().split()]
    orderly_array, inversions = merge(array)
    print(inversions)


if __name__ == '__main__':
    main()