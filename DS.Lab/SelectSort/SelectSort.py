# Selection sort in Python
import pickle
import time


def selectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = []
with open("my_list.pkl", "rb") as f:
    data = pickle.load(f)

size = len(data)
start = time.process_time()
selectionSort(data, size)
end = time.process_time()
print(f'Sorted Array in Ascending Order:{end - start}')
print(data)