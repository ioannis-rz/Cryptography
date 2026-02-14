import string

def encrypt(key, message):
  key = KEY.lower()
  message = message.lower()
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

  print(characters)

  for i in range(5):
    keyMatrix[i] = characters[5*i:(5*i)+5]

  return keyMatrix

def decrypt(key, encryptedMessage):
  decryptedMessage = ""
  return decryptedMessage

## test bench
print(generateMatrix("YoanPinzon"))
