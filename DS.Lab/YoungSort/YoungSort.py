import math
import pickle
import sys
import random
import time

sys.setrecursionlimit(100000)


def divide_to_rc(n):
    row = int(math.sqrt(n))

    while (n % row) != 0:
        row -= 1
    col = int(n / row)

    return row, col


class RowPictureYoungTable():
    def __init__(self, table, row, column):
        self.array = table
        self.row = row
        self.column = column
        self.visited = []

    def idx2rc(self, k):
        i = k // self.column
        j = k % self.column
        return (i, j)

    def rc2idx(self, i, j):
        return i * self.column + j

    def get_at(self, i, j):
        if (i >= self.row) or (j >= self.column):
            return -1
        return self.array[self.rc2idx(i, j)]

    def set_at(self, i, j, k):
        self.array[self.rc2idx(i, j)] = k

    def __str__(self):
        result = ""
        for i in range(self.row):
            flag = True
            for j in range(self.column):

                if flag:
                    result += "%3s" % str(self.get_at(i, j))
                    flag = False
                else:
                    result += ", %3s" % str(self.get_at(i, j))

            result += "\n"
        return result

    def sift_down(self, i, j):
        next_col = self.get_at(i, j + 1)
        next_row = self.get_at(i + 1, j)

        max_neighbor = (0, 0)
        if next_col > next_row:
            max_neighbor = (i, j + 1)
        else:
            max_neighbor = (i + 1, j)

        if self.get_at(i, j) < self.get_at(max_neighbor[0], max_neighbor[1]):
            (self.array[self.rc2idx(i, j)], self.array[self.rc2idx(max_neighbor[0], max_neighbor[1])]) = (
                self.array[self.rc2idx(max_neighbor[0], max_neighbor[1])], self.array[self.rc2idx(i, j)])

            self.sift_down(max_neighbor[0], max_neighbor[1])

    def sort_sift_down(self, i, j):
        next_col = self.get_at(i, j + 1)
        next_row = self.get_at(i + 1, j)

        max_neighbor = (0, 0)
        if next_row > next_col and (i + 1, j) not in self.visited:
            max_neighbor = (i + 1, j)
        elif (i, j + 1) not in self.visited:
            max_neighbor = (i, j + 1)
        else:
            return

        if self.get_at(i, j) < self.get_at(max_neighbor[0], max_neighbor[1]):
            (self.array[self.rc2idx(i, j)], self.array[self.rc2idx(max_neighbor[0], max_neighbor[1])]) = (
                self.array[self.rc2idx(max_neighbor[0], max_neighbor[1])], self.array[self.rc2idx(i, j)])

            self.sort_sift_down(max_neighbor[0], max_neighbor[1])

    def BuildYoungTable(self):
        for i in range(self.row - 1, -1, -1):
            for j in range(self.column - 1, -1, -1):
                self.sift_down(i, j)

    def young_sort(self):
        self.BuildYoungTable()

        for i in range(self.row - 1, -1, -1):
            for j in range(self.column - 1, -1, -1):
                # swap
                (self.array[self.rc2idx(i, j)], self.array[0]) = (self.array[0], self.array[self.rc2idx(i, j)])

                # adding i,j to visited
                self.visited.append((i, j))

                # sift down 0,0
                self.sort_sift_down(0, 0)

    def test(self):
        for i in range(0, self.row):
            for j in range(0, self.column - 1):
                if self.get_at(i, j) > self.get_at(i, j + 1):
                    return False
        for i in range(0, self.column):
            for j in range(0, self.row - 1):
                if self.get_at(j, i) > self.get_at(j + 1, i):
                    return False
        return True

def random_list(n=10, a=0, b=20):
    return [random.randint(a, b) for i in range(n)]

def random_permutation(a=0, b=10):
    l = [i for i in range(a, b)]
    random.shuffle(l)
    return l

def random_strings(count=10, string_size=5):
    chars = [chr(i) for i in range(97, 123)]

    res = []
    for i in range(count):
        a = ''.join(random.choices(chars, k=string_size))
        res.append(a)

    return res


if __name__ == '__main__':


    random_array = random_list(16900, 0, 10000000)
    with open('young_table.pkl', 'wb') as file:
        pickle.dump(random_array, file)

    # print("Before:", random_array)

    # young_table = RowPictureYoungTable(random_array, 120, 120)
    # start = time.time()
    # young_table.BuildYoungTable()
    # young_table.young_sort()
    # end = time.time()

    # print("After: ", young_table.array)
    # print("Time: ", end - start)
    # print(young_table.test())