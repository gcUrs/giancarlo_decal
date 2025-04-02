import numpy as np

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def containsPrimes(arr):
    return np.array([row for row in arr if any(is_prime(x) for x in row)])

def checkerboard():
    board = np.zeros((8, 8), dtype = int)
    board[::2, ::2] = 1
    board[1::2, 1::2] = 1
    return board

def r_checkerboard():
    board = np.zeros((8, 8), dtype=int)
    board[::2, 1::2] = 1
    board[1::2, ::2] = 1
    return board

def expansion(arr, n):
    return np.array([' '.join(list(word)). replace(' ', ' ' * n) for word in arr])

def secondDimmest(arr):
    return np.sort(arr, axis = 0) [1]
