import random


def shift(array):
    for i in range(len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array


def merge(array):
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


def count(array):
    length = len(array)
    max_num = max(array) + 1
    counting = [0] * max_num
    for i in range(length):
        counting[array[i]] += 1
    
    counter = 0
    for num in range(max_num):
        for i in range(counting[num]):
            array[counter] = num
            counter += 1
    return array


def swap(array, left, right):
    pivots = array[random.randrange(left, right)]
    s, m, n = left, left, right - 1
    while s <= n:
        if array[s] < pivots:
            array[s], array[m] = array[m], array[s]
            m += 1
            s += 1
        elif array[s] > pivots:
            array[s], array[n] = array[n], array[s]
            n -= 1
        else:
            s += 1
    return m, n


def quick(array, left, right):
    if right - left <= 1:
        return array
    
    m, n = swap(array, left, right)

    quick(array, left, m)
    quick(array, n + 1, right)

    return array


def get_kth(array, left, right, k):
    if k >= right:
        return -1
    elif right - left <= 1:
        return array[left]
    
    m, n = swap(array, left, right)

    if k < m:
        return get_kth(array, left, m, k)
    elif k >= n + 1:
        return get_kth(array, n + 1, right, k)
    else:
        return array[k]


def main():
    array = [random.randrange(0, 15) for x in range(0, 15)]

    index = random.randrange(0, len(array))
    kth_value = get_kth(array.copy(), 0, len(array), index)

    print('Array:\t', array)
    print('Shift:\t', shift(array.copy()))
    print('Merge:\t', merge(array.copy()))
    print('Count:\t', count(array.copy()))
    print('Quick:\t', quick(array, 0, len(array)))

    print('Return KTH:', kth_value)
    print('Checks KTH:', array[index])


if __name__ == '__main__':
    main()


