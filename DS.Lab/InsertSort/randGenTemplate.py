import random
import pickle


def randList(seed, n):
  random.seed(seed)
  return [random.randint(0,1000000000) for x in range(n)]

n = 30000
# print(randList(1401,n))



with open('my_list.pkl', 'wb') as file:
    pickle.dump(randList(1401, n), file)