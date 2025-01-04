import pickle
import time


def partition(arr, low, high):
    # Choose the pivot
    pivot = arr[(high + low) // 2]

    arr[low], arr[high] = arr[high], arr[low]

    i = low - 1

    # Traverse arr[low..high] and move all smaller
    # elements on the left side. Elements from low to
    # i are smaller after every iteration
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Move pivot after smaller elements and
    # return its position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# The QuickSort function implementation
def quick_sort(arr, low, high):
    if low < high:
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)

        # Recursion calls for smaller elements
        # and greater or equals elements
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# Function to print an array
def print_array(arr):
    for i in arr:
        print(i, end=" ")
    print()


# Driver code
if __name__ == "__main__":
    arr = []
    with open("my_list_best_case.pkl", "rb") as f:
        arr = pickle.load(f)
    # print("Given array is")
    # print_array(arr)

    start_best = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    end_best = time.time()
    print(f"Quick sort took {end_best - start_best} seconds")
    # print("\nSorted array is")
    # print_array(arr)

    # ------------------------------------------------------------------------------
    arr = []
    with open("my_list_worst_case.pkl", "rb") as f:
        arr = pickle.load(f)

    start_worst = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    end_worst = time.time()
    print(f"Quick sort took {end_worst - start_worst} seconds")

    # #-------------------------------------------------------------------------------

    arr = []
    with open("my_list_rand_case.pkl", "rb") as f:
        arr = pickle.load(f)

    start_rand = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    end_rand = time.time()
    print(f"Quick sort took {end_rand - start_rand} seconds")