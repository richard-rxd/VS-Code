# implementation of quick sort in python using hoare partition scheme

def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def quick_sort(elements, low, high):
    if low >= high or low < 0:
        return
    
    if low < high:
        pi = partition(elements, low, high)
        quick_sort(elements, low, pi-1)
        quick_sort(elements, pi+1, high)

def partition(elements, low, high):
    pivot = elements[high]
    i = low

    for j in range(low, high):
        if elements[j] <= pivot:
            swap(j, i, elements) # Entweder wird die Zahl mit sich selbst geswapt oder mit der ersten Zahl im Array die größer ist
            i += 1 # i zeigt immer auf die erste Zahl im Array die größer ist als der Pivot (Falls es eine größere Zahl gibt)
    
    swap(i, high, elements)

    return i

if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6],
        [29, 15, 29, 15, 4, 9, 4],
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')