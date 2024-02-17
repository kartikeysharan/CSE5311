import heapq

def merge_sorted_arrays(arrays):
    merged_result = []
    heap = []

    # Initialize heap with the first element from each array
    for i, array in enumerate(arrays):
        if array:  # Ensure the array is not empty
            heapq.heappush(heap, (array[0], i, 0))  # Push (element, array_index, element_index)

    while heap:
        val, array_index, element_index = heapq.heappop(heap)
        merged_result.append(val)

        # Move to the next element in the array
        if element_index + 1 < len(arrays[array_index]):
            next_val = arrays[array_index][element_index + 1]
            heapq.heappush(heap, (next_val, array_index, element_index + 1))

    return merged_result
