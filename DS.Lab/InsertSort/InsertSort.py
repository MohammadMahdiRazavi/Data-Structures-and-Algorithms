# Insertion sort in Python
import pickle
import time


def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key


data = []
with open("my_list.pkl", "rb") as f:
    data = pickle.load(f)
start = time.process_time()
insertionSort(data)
end = time.process_time()
print(f'Sorted Array in Ascending Order:{end - start}')
print(data)