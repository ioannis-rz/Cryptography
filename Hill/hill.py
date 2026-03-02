import numpy as np

def hill(key, cyphertext):
    cleartext=""
    return cleartext

def hill(key, cleartext):
    cyphertext = ""
    return cyphertext

def det(matrix: np.array):
    det = np.linalg.det(matrix)
    return det

def hasInverse(matrix: np.array):
    if (matrix.shape != (2,2)):
        raise Exception("Matrix size must be 2x2")
    if (det(matrix) != 0):
        return True
    else: return False

test2 = np.array([[2,1],[1,1]])
test = np.zeros((2,2), dtype=int)
print(det(test2))

print(hasInverse(test2))
