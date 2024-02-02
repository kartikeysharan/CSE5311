import sys
import time
import random
import matplotlib.pyplot as plt

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

def generate_dataset(size):
    return [random.randint(1, 5000000) for _ in range(size)]

if __name__ == "__main__":

    dataset_sizes = [5,10,20,50,100,500,5000,10000,20000,30000,40000,50000] 
    runtimes = []

    for dataset_size in dataset_sizes:

        dataset = generate_dataset(dataset_size)

        print(f"Generated a dataset with {dataset_size} elements.")

        # Measure the runtime of selection_sort
        start_time = time.time()
        selection_sort(dataset)
        end_time = time.time()
        runtime = end_time - start_time
        runtimes.append(runtime)

        print(f"Runtime for dataset size {dataset_size}: {runtime} seconds")

    # Plotting the results
    plt.plot(dataset_sizes, runtimes, marker='o')
    plt.title('Selection Sort Runtime for Different Array Sizes')
    plt.xlabel('Array Size')
    plt.ylabel('Runtime (seconds)')
    plt.show()
