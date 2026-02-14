import string

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

  characters = key + characters

  for i in range(26):
    if characters[i] == 'i':
      characters[i] = 'ij'
      characters.remove('j')
      break
    elif characters[i] == 'j':
      characters[i] = 'ij'
      characters.remove('i')
      break

  for i in range(5):
    keyMatrix[i] = characters[5*i:(5*i)+5]

  return keyMatrix

def encrypt(key, message):
  key = key.lower()
  matrix = generateMatrix(key)
  print(matrix)
  print(matrix[0][0])
  message = message.lower()
  encryptedMessage = ""
  table = generateMatrix(key)

  return encryptedMessage

def decrypt(key, encryptedMessage):
  decryptedMessage = ""
  return decryptedMessage

# test bench
encrypt("YoanPinzon", "OU RF RI EN DF RO MP AR IS")
