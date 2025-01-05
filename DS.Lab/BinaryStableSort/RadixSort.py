import random
import time

def rand_list(seed, n):
    random.seed(seed)
    return [random.randint(0, 10000000) for _ in range(n)]

def block_swap(A, p, q, n):
    for i in range(n):
        A[p + i], A[q + i] = A[q + i], A[p + i]

def stable_rba(A, p, q, r):
    n0 = r - q
    n1 = q - p
    if n1 == 0:
        return r
    while n0 > 0:
        if n1 > n0:
            p = q - n0
            block_swap(A, p, q, n0)
            n1 -= n0
            q = p
            p -= n1
        else:
            block_swap(A, p, q, n1)
            n0 -= n1
            p = q
            q += n1
    return p

def radix_key(x, mask):
    return x & mask

def binary_stable_sort(A, p, r, mask):
    if r - p > 1:
        q = (p + r) // 2
        p = binary_stable_sort(A, p, q, mask)
        r = binary_stable_sort(A, q, r, mask)
        p = stable_rba(A, p, q, r)
    elif radix_key(A[p], mask) == 0:
        return r
    return p

def inplace_radix_sort(A, n):
    mask = 1
    for _ in range(32):
        binary_stable_sort(A, 0, n, mask)
        mask <<= 1

if __name__ == "__main__":
    n = 10000000
    A = rand_list(1401, n)

    start = time.time()
    inplace_radix_sort(A, n)
    end = time.time()
    radix_time = end - start

    print(f"Time taken: {radix_time} seconds")
