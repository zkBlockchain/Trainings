class Heap_Min:
    def __init__(self):
        self.array = []
        self.len = 0
    
    def remove_min(self):
        min_value = self.array[0]
        self.array[0], self.array[self.len - 1] = self.array[self.len - 1], self.array[0]
        self.array.pop()
        self.len -= 1
        i = 0
        while (2 * i) + 1 < self.len:
            j = (2 * i) + 1
            if (2 * i) + 2 < self.len and self.array[(2 * i) + 2] < self.array[j]:
                j = (2 * i) + 2
            if self.array[i] <= self.array[j]:
                break
            else:
                self.array[i], self.array[j] = self.array[j], self.array[i]
                i = j
        return min_value

    def insert(self, elem):
        self.array.append(elem)
        self.len += 1
        i = len(self.array) - 1
        while i > 0 and self.array[i] < self.array[(i - 1) // 2]:
            self.array[i], self.array[(i - 1) // 2] = self.array[(i - 1) // 2], self.array[i]
            i = (i - 1) // 2


class Heap_Max:
    def __init__(self):
        self.array = []
        self.len = 0

    def remove_max(self):
        max_value = self.array[0]
        self.array[0], self.array[self.len - 1] = self.array[self.len - 1], self.array[0]
        self.array.pop()
        self.len -= 1
        i = 0
        while (2 * i) + 1 < self.len:
            j = (2 * i) + 1
            if (2 * i) + 2 < self.len and self.array[(2 * i) + 2] > self.array[j]:
                j = (2 * i) + 2
            if self.array[i] >= self.array[j]:
                break
            else:
                self.array[i], self.array[j] = self.array[j], self.array[i]
                i = j
        return max_value

    def insert(self, elem):
        self.array.append(elem)
        self.len += 1
        i = len(self.array) - 1
        while i > 0 and self.array[i] > self.array[(i - 1) // 2]:
            self.array[i], self.array[(i - 1) // 2] = self.array[(i - 1) // 2], self.array[i]
            i = (i - 1) // 2


def main():
    tasks = int(input())
    sorting = Heap_Max()
    for _ in range(tasks):
        task = [int(x) for x in input().split()]
        if task[0] == 0:
            sorting.insert(task[1])
        else:
            print(sorting.remove_max())


if __name__ == '__main__':
    main()