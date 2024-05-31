def shell_sort(arr):
    size = len(arr)
    gap = size//2

    while gap > 0:
        duplicate_index = []
        for i in range(gap,size):
            anchor = arr[i]
            j = i
            while j>=gap and arr[j-gap]>=anchor:
                if arr[j-gap] == anchor:
                    duplicate_index.append(j)
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        duplicate_index = list(set(duplicate_index))
        duplicate_index.sort()
        if duplicate_index:
            for i in duplicate_index[-1::-1]:
                del arr[i]

        size = len(arr)
        gap = gap // 2


if __name__ == '__main__':
    tests = [
        [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    ]
    elements = [89,78,61,53,23,21,17,12,9,7,6,2,1]
    for elements in tests:
        shell_sort(elements)
        print(elements)
        """

def shell_sort(arr):
    n = len(arr)
    div = 2
    gap = n//div
    while gap > 0:
        index_to_delete = []
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] >= temp:
                if arr[j-gap] == temp:
                    index_to_delete.append(j)
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        index_to_delete=list(set(index_to_delete))
        index_to_delete.sort()
        if index_to_delete:
            for i in index_to_delete[-1::-1]:
                del arr[i]
        div *= 2
        n = len(arr)
        gap = n//div


if __name__ == '__main__':
    elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9,  5, 8, 3]

    print(f'Given unsorted list: {elements}')
    shell_sort(elements)
    print(f'List after Sorting : {elements}')"""