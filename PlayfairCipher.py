import string

def encrypt(key, message):
  key = ""
  encryptedMessage = ""
  table = generateMatrix(key,5)

  return encryptedMessage

def generateMatrix(key):
  keyMatrix = [
              [],
              [],
              [],
              [],
              []
              ]
  key = list(key.lower())
  characters = list(string.ascii_lowercase)
  temp1 = len(key)

  temp = 0

  for i in range(temp1):
    try:
      characters.remove(key[i])
    except ValueError:
      key[i] = 0
      temp += 1

  for i in range(temp):
    key.remove(0)

  keySize = len(key)
  print(keySize)
  temp = 5
  temp1 = 0

  for i in range(keySize//5 + keySize%5 + 1):
    keyMatrix[i] = list(key[temp1:temp])
    temp1 += 5
    temp += 5
  for i in range(keySize//5 + keySize%5, 5):
    keyMatrix[i] = list(characters[0:5])


  return keyMatrix

def decrypt(key, encryptedMessage):
  decryptedMessage = ""
  return decryptedMessage

## test bench
print(generateMatrix("YoanPinzon"))
