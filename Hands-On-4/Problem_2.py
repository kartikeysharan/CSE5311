def remove_duplicates(arr):
    if not arr:
        return []

    unique_elements = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            unique_elements.append(arr[i])

    return unique_elements
