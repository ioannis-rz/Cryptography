import numpy as np
import re

def decryptHill(key: np.array, ciphertext: str):
    cleartext=""
    return cleartext

def encryptHill(key: np.array, cleartext: str):
    cleartext = re.sub("[^A-Za-z]", "", cleartext).lower()
    if len(cleartext) % 2 != 0:
        cleartext += 'x'
    ciphertext = ""
    for i in range(0, len(cleartext), 2):
        temp = np.array([ord(cleartext[i]) - ord('a'), ord(cleartext[i+1]) - ord('a')])
        temp = np.matmul(temp,key) % 26
        ciphertext += chr(temp[0] + ord('a')) + chr(temp[1] + ord('a'))
    return ciphertext

def hasInverse(matrix: np.array):
    if (matrix.shape != (2,2)):
        raise Exception("Matrix size must be 2x2")
    if (int(np.linalg.det(matrix)) != 0):
        return True
    else: return False

test2 = np.array([[11,8],[3,7]])
text = "JULY"
cipher = encryptHill(test2, text)
print(cipher)
