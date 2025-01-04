# Bubble sort in Python
import pickle
import time


def bubbleSort(array):
    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


data = []
with open("my_list.pkl", "rb") as f:
    data = pickle.load(f)

st = time.process_time()
bubbleSort(data)
et = time.process_time()

print(f'Sorted Array in Ascending Order:{et - st}')
print(data)