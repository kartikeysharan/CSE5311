import sys
import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def generate_dataset(size):
    return [random.randint(1, 5000000) for _ in range(size)]

if __name__ == "__main__":

    dataset_sizes = [5,10,20,50,100,500,5000,10000,20000,30000,40000,50000] 
    runtimes = []

    for dataset_size in dataset_sizes:

        dataset = generate_dataset(dataset_size)

        print(f"Generated a dataset with {dataset_size} elements.")

        # Measure the runtime of bubble_sort
        start_time = time.time()
        bubble_sort(dataset)
        end_time = time.time()
        runtime = end_time - start_time
        runtimes.append(runtime)

        print(f"Runtime for dataset size {dataset_size}: {runtime} seconds")

    # Plotting the results
    plt.plot(dataset_sizes, runtimes, marker='o')
    plt.title('Bubble Sort Runtime for Different Array Sizes')
    plt.xlabel('Array Size')
    plt.ylabel('Runtime (seconds)')
    plt.show()
