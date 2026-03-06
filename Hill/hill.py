import numpy as np
import re

ALPHABET_SIZE = 26

def decryptHill(key: np.array, ciphertext: str):
    cleartext=""
    ciphertext = cleanText(ciphertext)
    if len(ciphertext) % 2 != 0:
        raise ValueError("Longitud del ciphertext debe ser par")

    keyInv = inverseModular(key, ALPHABET_SIZE)

    for i in range(0, len(ciphertext), 2):
        temp = np.array([ord(ciphertext[i]) - ord('a'), ord(ciphertext[i+1]) - ord('a')])
        temp = np.matmul(temp,keyInv) % ALPHABET_SIZE
        cleartext += chr(temp[0] + ord('a')) + chr(temp[1] + ord('a'))
    return cleartext

def encryptHill(key: np.array, cleartext: str):
    ciphertext = ""
    cleartext = cleanText(cleartext)
    if len(cleartext) % 2 != 0:
        cleartext += 'x'

    if key.shape != (2,2):
        raise ValueError("Matriz debe ser 2x2")
    if (eea(det(key),ALPHABET_SIZE)[0]) != 1:
        raise ValueError("Matriz no tiene inversa modular")

    for i in range(0, len(cleartext), 2):
        temp = np.array([ord(cleartext[i]) - ord('a'), ord(cleartext[i+1]) - ord('a')])
        temp = np.matmul(temp,key) % ALPHABET_SIZE
        ciphertext += chr(temp[0] + ord('a')) + chr(temp[1] + ord('a'))
    return ciphertext

def det(matrix: np.array):
    if (matrix.shape != (2,2)):
        raise ValueError("Matriz debe tener tamaño 2x2")
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

def adj(matrix: np.array):
    if (matrix.shape != (2,2)):
        raise ValueError("Matriz debe tener tamaño 2x2")
    adjMatrix = matrix.copy()
    adjMatrix[0][0] = matrix[1][1]
    adjMatrix[1][1] = matrix[0][0]
    adjMatrix[0][1] = -matrix[0][1]
    adjMatrix[1][0] = -matrix[1][0]
    return adjMatrix

def eea(a: int, b: int):
    if b == 0:
        return (a, 1, 0)
    (d, x, y) = eea(b, a % b)
    q = a // b
    (d, x, y) = (d, y, x - q * y)
    return (d, x, y)

def cleanText(text: str):
    textCorrected = re.sub("[^A-Za-z]", "", text).lower()
    return textCorrected

def inverseModular(matrix: np.array, mod: int):
    if matrix.shape != (2,2):
        raise ValueError("Matriz debe ser 2x2")
    eeaResult = eea(det(matrix), mod)
    if eeaResult[0] != 1:
        raise ValueError("Matriz no tiene inversa modular")
    mat = adj(matrix)
    return (mat * eeaResult[1]) % mod

test2 = np.array([[11,8],[3,7]])
text = "JULY"
cipher = encryptHill(test2, text)
cleartext = decryptHill(test2, cipher)
print("Ciphertext: " + cipher)
print("Cleartext: " + cleartext)
