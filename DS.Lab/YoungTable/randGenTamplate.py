import random
import pickle

def randList(seed, n):
    random.seed(seed)
    my_list = [random.randint(0,100000) for x in range(n)]
    return my_list

n = 160000

with open('young_table.pkl', 'wb') as file:
    pickle.dump(randList(1401, n), file)