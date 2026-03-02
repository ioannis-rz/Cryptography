import numpy as np

def decryptHill(key, cyphertext):
    cleartext=""
    return cleartext

def encryptHill(key, cleartext):
    cyphertext = ""
    return cyphertext

def hasInverse(matrix: np.array):
    if (matrix.shape != (2,2)):
        raise Exception("Matrix size must be 2x2")
    if (int(np.linalg.det(matrix)) != 0):
        return True
    else: return False

test2 = np.array([[11,8],[3,7]])
print(int(np.linalg.det(test2)))
print(hasInverse(test2))
