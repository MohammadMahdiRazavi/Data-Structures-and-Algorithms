import pickle
import sys
import time


class youngTable:
    def __init__(self, table: list, row: int, col: int):
        self.table = table
        self.row = row
        self.col = col
        self.size = row * col


    def idx2rc(self, index):
        return ((index // self.col), index % self.col)


    def rc2idx(self, row, col):
        if row * self.col + col > self.size:
            return None
        return (row * self.col + col)


    def getAt(self, row, col):
        return self.table[row * self.col + col]


    def setAt(self, row, col, value):
        self.table[row * self.col + col] = value


    def siftDown(self, row, col):

        currentNum = self.getAt(row, col)

        if row < self.row - 1:
            downNeighbor = self.getAt(row + 1, col)
            existDown = True
        else:
            existDown = False

        if col < self.col - 1:
            rightNeighbor = self.getAt(row, col + 1)
            existRight = True
        else:  # col = self.col - 1
            existRight = False

        if (existDown and existRight):
            maxNeighbor = max(downNeighbor, rightNeighbor)
        elif (existRight):
            maxNeighbor = rightNeighbor
        elif (existDown):
            maxNeighbor = downNeighbor
        else:
            return
        if currentNum < maxNeighbor:
            if existRight and existDown and maxNeighbor == rightNeighbor:
                self.setAt(row, col, maxNeighbor)
                self.setAt(row, col + 1, currentNum)
                self.siftDown(row, col + 1)
            elif existRight and existDown and maxNeighbor == downNeighbor:
                self.setAt(row, col, maxNeighbor)
                self.setAt(row + 1, col, currentNum)
                self.siftDown(row + 1, col)
            elif existRight:
                self.setAt(row, col, maxNeighbor)
                self.setAt(row, col + 1, currentNum)
                self.siftDown(row, col + 1)
            elif existDown:
                self.setAt(row, col, maxNeighbor)
                self.setAt(row + 1, col, currentNum)
                self.siftDown(row + 1, col)
        else:
            return


    def buildYoungTable(self):
        for i in range(self.row - 1, -1, -1):
            for j in range(self.col - 1, -1, -1):
                self.siftDown(i, j)


    def printYoungTable(self):
        for i in range(len(self.table)):
            if i % self.col == 0 and i != 0:
                print('')
            print(self.table[i], end=' ')
        print('')


    def test(self):
        for i in range(0, self.row):
            for j in range(0, self.col - 1):
                if self.getAt(i, j) < self.getAt(i, j + 1):
                    return False
        for i in range(0, self.col):
            for j in range(0, self.row - 1):
                if self.getAt(j, i) < self.getAt(j + 1, i):
                    return False
        return True

if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    table = []
    with open('young_table.pkl', 'rb') as f:
        table = pickle.load(f)
    yt = youngTable(table, 400, 400)
    start = time.time()
    yt.buildYoungTable()
    end = time.time()
    print(yt.test())
    print(end - start)
    # yt.printYoungTable()