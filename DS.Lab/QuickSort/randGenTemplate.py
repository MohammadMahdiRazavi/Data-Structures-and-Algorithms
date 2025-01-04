import random
import pickle

def randListWorst(seed, n):
  random.seed(seed)
  worst_case = [random.randint(0,100000) for x in range(n)]
  worst_case = sorted(worst_case)
  rev_worst_case = worst_case[::-1]
  return rev_worst_case

def randListbest(seed, n):
  random.seed(seed)
  best_case = [random.randint(0,100000) for x in range(n)]
  best_case = sorted(best_case)
  return best_case

def randList(seed, n):
  random.seed(seed)
  my_list = [random.randint(0,100000) for x in range(n)]
  return my_list

n = 300000
# print(randList(1401,n))
# here we save it to .pkl file using pickle library
with open('my_list_worst_case.pkl', 'wb') as file:
  pickle.dump(randListWorst(1401, n), file)


with open('my_list_best_case.pkl', 'wb') as file:
  pickle.dump(randListbest(1401, n), file)

with open('my_list_rand_case.pkl', 'wb') as file:
  pickle.dump(randList(1401, n), file)