
def merge_sort(arr, key, descending=False):
    if len(arr) <= 1:
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left, key, descending)
    merge_sort(right, key, descending)

    merge_two_sorted_lists(left, right, arr, key, descending)

def merge_two_sorted_lists(a,b,arr,key, descending):
    k = 0

    while 0 < len(a) and 0 < len(b):
        if descending:
            if a[0][key] >= b[0][key]:
                arr[k] = a.pop(0)
            else:
                arr[k] = b.pop(0)
            k += 1
        else:
            if a[0][key] <= b[0][key]:
                arr[k] = a.pop(0)
            else:
                arr[k] = b.pop(0)
            k += 1

    arr.extend(a)
    arr.extend(b)

if __name__ == '__main__':
    elements = [
            { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
            { 'name': 'rajab', 'age': 12,  'time_hours': 3},
            { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
            { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
        ]

    merge_sort(elements, key='time_hours', descending=True)
    print(elements, "\n")
    merge_sort(elements, key='name')
    print(elements, "\n")