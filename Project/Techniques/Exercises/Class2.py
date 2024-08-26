'''
1. De acordo com o array X = np.array([3, 5, 6, 7, 2, 3, 4, 9, 4])
faça a soma
2. Faça a média
3. Dada a matriz faça a soma das colunas X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
4. Faça a média das linhas
5. Dado o array X = np.array([1, 2, 0, 4, 5, 6, 0, 0, 9, 10])
Mostre o elemento de maior valor'''

import numpy as np

# 1 - De acordo com o array X = np.array([3, 5, 6, 7, 2, 3, 4, 9, 4]) faça a soma
X = np.array([3, 5, 6, 7, 2, 3, 4, 9, 4])
print(np.sum(X))

# 2 - Faça a média
X = np.array([3, 5, 6, 7, 2, 3, 4, 9, 4])
print(np.mean(X))

# 3 - Dada a matriz faça a soma das colunas X = np.array([ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16] ])
X = np.array([ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16] ])
print(np.sum(X, axis=0))

# 4 - Faça a média das linhas
X = np.array([ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16] ])
print(np.sum(X, axis=1))

X = np.array([1, 2, 0, 4, 5, 6, 0, 0, 9, 10])
print(np.max(X))