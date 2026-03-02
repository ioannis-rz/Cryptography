import numpy as np
import re

ALPHABET_SIZE = 26

def decryptHill(key: np.array, ciphertext: str):
    cleartext=""
    keyInv = inverseModular(key, ALPHABET_SIZE)
    for i in range(0, len(ciphertext), 2):
        temp = np.array([ord(ciphertext[i]) - ord('a'), ord(ciphertext[i+1]) - ord('a')])
        temp = np.matmul(temp,keyInv) % ALPHABET_SIZE
        cleartext += chr(temp[0] + ord('a')) + chr(temp[1] + ord('a'))
    return cleartext

def encryptHill(key: np.array, cleartext: str):
    cleartext = re.sub("[^A-Za-z]", "", cleartext).lower()
    if len(cleartext) % 2 != 0:
        cleartext += 'x'
    ciphertext = ""
    for i in range(0, len(cleartext), 2):
        temp = np.array([ord(cleartext[i]) - ord('a'), ord(cleartext[i+1]) - ord('a')])
        temp = np.matmul(temp,key) % ALPHABET_SIZE
        ciphertext += chr(temp[0] + ord('a')) + chr(temp[1] + ord('a'))
    return ciphertext

def det(matrix: np.array):
    if (matrix.shape != (2,2)):
        raise Exception("Matriz debe tener tamaño 2x2")
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

def adjunta(matrix: np.array):
    if (matrix.shape != (2,2)):
        raise Exception("Matriz debe tener tamaño 2x2")
    temp = matrix[0][0]
    matrix[0][0] = matrix[1][1]
    matrix[1][1] = temp
    matrix[0][1] = -matrix[0][1]
    matrix[1][0] = -matrix[1][0]
    return matrix

def hasInverse(matrix: np.array):
    if (det(matrix) != 0):
        return True
    else: return False

def eea(a: int, b: int):
    if b == 0:
        return (a, 1, 0)
    (d, x, y) = eea(b, a % b)
    q = a // b
    (d, x, y) = (d, y, x - q * y)
    return (d, x, y)

def inverseModular(matrix: np.array, mod: int):
    if not hasInverse(matrix):
        raise Exception("La matriz no tiene inversa")
    mat = adjunta(matrix)
    return (mat * eea(det(matrix), mod)[1]) % mod

test2 = np.array([[3,7],[5,12]])
text = "Herbert Yardley wrote The American Black Chamber"
cipher = encryptHill(test2, text)
#print(adjunta(test2))
#print(det(test2))
# print(inverseModular(test2, 26))
cleartext = decryptHill(test2, cipher)
print("Ciphertext: " + cipher)
print("Cleartext: " + cleartext)