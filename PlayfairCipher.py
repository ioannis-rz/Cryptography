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

def encrypt(key, cleartext):

  key = key.lower()
  cleartext = cleartext.lower()
  matrix = generateMatrix(key)
  indexDict = dict()
  ciphertext = ""

  # generar matriz de indices para consulta
  for i in range(5):
    for j in range(5):
      indexDict[matrix[i][j]]=(i,j)

  # para la pareja de caracteres
  if cleartext[0] == 'i' or cleartext[0] == 'j':
    indexChar1 = indexDict.get("ij")
  else:
    indexChar1 = indexDict.get(cleartext[0])
  if cleartext[1] == 'i' or cleartext[1] == 'j':
    indexChar2 = indexDict.get("ij")
  else:
    indexChar2 = indexDict.get(cleartext[1])

  #caso misma fila
  if indexChar1[0] == indexChar2[0]:
    char = matrix[indexChar1[0]][(indexChar1[1]+1)%5]
    ciphertext = ciphertext + char
    char = matrix[indexChar2[0]][(indexChar2[1]+1)%5]
    ciphertext = ciphertext + char

  #caso misma columna
  elif indexChar1[1] == indexChar2[1]:
    char = matrix[(indexChar1[0]+1)%5][indexChar1[1]]
    ciphertext = ciphertext + char
    char = matrix[(indexChar2[0]+1)%5][indexChar2[1]]
    ciphertext = ciphertext + char

  # rectangulo
  elif indexChar1[0] != indexChar2[0] and indexChar1[1] != indexChar2[1]:
    char = matrix[indexChar1[0]][indexChar2[1]]
    ciphertext = ciphertext + char
    char = matrix[indexChar2[0]][indexChar1[1]]
    ciphertext = ciphertext + char

  # por si acaso
  else:
    print("los caracteres son los mismos")


  return ciphertext

def decrypt(key, ciphertext):
  key = key.lower()
  cleartext = ""
  matrix = generateMatrix(key)
  indexDict = dict()
  ciphertext = ciphertext.lower()

  # generar matriz de indices para consulta
  for i in range(5):
    for j in range(5):
      indexDict[matrix[i][j]]=(i,j)

  # para la pareja de caracteres
  if ciphertext[0] == 'i' or ciphertext[0] == 'j':
    indexChar1 = indexDict.get("ij")
  else:
    indexChar1 = indexDict.get(ciphertext[0])
  if ciphertext[1] == 'i' or ciphertext[1] == 'j':
    indexChar2 = indexDict.get("ij")
  else:
    indexChar2 = indexDict.get(ciphertext[1])

  #caso misma fila
  if indexChar1[0] == indexChar2[0]:
    char = matrix[indexChar1[0]][(indexChar1[1]-1)%5]
    cleartext = cleartext + char
    char = matrix[indexChar2[0]][(indexChar2[1]-1)%5]
    cleartext = cleartext + char

  #caso misma columna
  elif indexChar1[1] == indexChar2[1]:
    char = matrix[(indexChar1[0]-1)%5][indexChar1[1]]
    cleartext = cleartext + char
    char = matrix[(indexChar2[0]-1)%5][indexChar2[1]]
    cleartext = cleartext + char

  # rectangulo
  elif indexChar1[0] != indexChar2[0] and indexChar1[1] != indexChar2[1]:
    char = matrix[indexChar1[0]][indexChar2[1]]
    cleartext = cleartext + char
    char = matrix[indexChar2[0]][indexChar1[1]]
    cleartext = cleartext + char

  # por si acaso
  else:
    print("los caracteres son los mismos")


  return cleartext



# test bench
print(encrypt("YoanPinzon", "OU RF RI EN DF RO MP AR IS"))
print(decrypt("YoanPinzon", "KI"))
