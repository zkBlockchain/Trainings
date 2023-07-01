#[0, 1, 2, 3, 3, 4, 4, 4, 5, 8, 9]
array = [3, 8, 1, 3, 4, 4, 4, 9, 0, 2, 5]

#[0, 1, 2, 3, 3, 3, 5, 5, 5, 6, 9, 9, 9]
array_1 = [5, 3, 9, 3, 9, 0, 5, 3, 1, 9, 2, 5, 6]

#[0, 0, 0, 0, 1, 4, 4, 5, 5, 6, 6, 9]
array_2 = [4, 4, 5, 5, 6, 6, 9, 0, 0, 0, 0, 1]
    
#[1, 1, 2, 2, 3, 3, 4, 4]
array_3 = [4, 3, 2, 1, 4, 3, 2, 1]


def shift(array):
    for i in range(len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array


def merge(array): # Recursion
    array_len = len(array)
    if not array_len or array_len == 1:
        return array
    if array_len == 2:
        if array[0] > array[1]:
            return [array[1], array[0]]
        else:
            return array
    
    left = merge(array[:array_len // 2])
    right = merge(array[array_len // 2:])
    left_len, right_len = len(left), len(right)
    
    n, m = 0, 0
    results = []
    while n < left_len or m < right_len:
        if left[n] < right[m]:
            results.append(left[n])
            n += 1
        else:
            results.append(right[m])
            m += 1

        if n == left_len:
            results.extend(right[m:])
            return results
        elif m == right_len:
            results.extend(left[n:])
            return results
    return results


def main():
    print(shift(array))
    print(merge(array))


if __name__ == '__main__':
    main()


