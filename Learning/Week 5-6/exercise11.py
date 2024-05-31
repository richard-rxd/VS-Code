def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index, found = []):
    if right_index < left_index:
        return found

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return found

    mid_number = numbers_list[mid_index]

    #Meine Lösung:

    """if mid_index in found:
        mid_right = mid_index
        mid_left = mid_index
        while numbers_list[mid_right] == number_to_find:
            mid_right += 1
            if numbers_list[mid_right] == number_to_find:
                found.append(mid_right)
        while numbers_list[mid_left] == number_to_find:
            mid_left -= 1
            if numbers_list[mid_left] == number_to_find:
                found.append(mid_left)
        return found
    else:
        if mid_number == number_to_find:
            found.append(mid_index)"""

    if mid_number == number_to_find:
        found.append(mid_index)
        # Expand to the left
        left = mid_index - 1
        while left >= 0 and numbers_list[left] == number_to_find:
            found.append(left)
            left -= 1
        # Expand to the right
        right = mid_index + 1
        while right < len(numbers_list) and numbers_list[right] == number_to_find:
            found.append(right)
            right += 1
        return found
    
    if mid_number < number_to_find:
        left_index = mid_index + 1
    elif mid_number > number_to_find:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

if __name__ == '__main__':
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15  

    index = binary_search_recursive(numbers, number_to_find, 0, len(numbers))
    print(f"Number found at index {index} using binary search")