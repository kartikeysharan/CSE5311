import sys
import time
import random
import matplotlib.pyplot as plt

def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def generate_dataset(size):
    return [random.randint(1, 5000000) for _ in range(size)]

if __name__ == "__main__":

    dataset_sizes = [5,10,20,50,100,500,5000,10000,20000,30000,40000,50000]  
    runtimes = []

    for dataset_size in dataset_sizes:

        dataset = generate_dataset(dataset_size)

        print(f"Generated a dataset with {dataset_size} elements.")

        # Measure the runtime of insertion_sort
        start_time = time.time()
        insertion_sort(dataset)
        end_time = time.time()
        runtime = end_time - start_time
        runtimes.append(runtime)

        print(f"Runtime for dataset size {dataset_size}: {runtime} seconds")

    # Plotting the results
    plt.plot(dataset_sizes, runtimes, marker='o')
    plt.title('Insertion Sort Runtime for Different Array Sizes')
    plt.xlabel('Array Size')
    plt.ylabel('Runtime (seconds)')
    plt.show()