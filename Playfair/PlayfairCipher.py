import string

def generateMatrix(key):
  keyMatrix = [
              [],
              [],
              [],
              [],
              []
              ]

  key = list(key.lower().replace('j','i'))
  characters = list(string.ascii_lowercase.replace('j',''))
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


  # for i in range(26):
  #   if characters[i] == 'i':
  #     characters[i] = 'ij'
  #     characters.remove('j')
  #     break
  #   elif characters[i] == 'j':
  #     characters[i] = 'ij'
  #     characters.remove('i')
  #     break

  for i in range(5):
    keyMatrix[i] = characters[5*i:(5*i)+5]

  return keyMatrix

def preprocessText(text):
    text = ''.join(char for char in text if char.isalpha()).lower()
    text = text.replace('j','i')
    result = []
    i = 0

    while i < len(text):
        char1 = text[i]

        # impar
        if i + 1 >= len(text):
            result.append(char1 + 'x')
            break

        char2 = text[i + 1]

        # dos letras iguales
        if char1 == char2:
            result.append(char1 + 'x')
            i += 1
        else:
            result.append(char1 + char2)
            i += 2
    return ''.join(result).replace(" ", "")

def encrypt(key, cleartext):

  key = key.lower()
  cleartext = preprocessText(cleartext)
  matrix = generateMatrix(key)
  indexDict = dict()
  ciphertext = ""

  # generar matriz de indices para consulta
  for i in range(5):
    for j in range(5):
      indexDict[matrix[i][j]]=(i,j)

  for k in range(0, len(cleartext), 2):

    # # para la pareja de caracteres
    # if cleartext[k] == 'i' or cleartext[k] == 'j':
    #   indexChar1 = indexDict.get("ij")
    # else:
    indexChar1 = indexDict.get(cleartext[k])
    # if cleartext[k+1] == 'i' or cleartext[k+1] == 'j':
    #   indexChar2 = indexDict.get("ij")
    # else:
    indexChar2 = indexDict.get(cleartext[k+1])

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
      print("Se presento un error")

  return ciphertext

def decrypt(key, ciphertext):

  key = key.lower()
  ciphertext = ciphertext.lower()
  matrix = generateMatrix(key)
  indexDict = dict()
  cleartext = ""


  # generar matriz de indices para consulta
  for i in range(5):
    for j in range(5):
      indexDict[matrix[i][j]]=(i,j)

  for k in range(0, len(ciphertext), 2):
    # para la pareja de caracteres
    indexChar1 = indexDict.get(ciphertext[k])
    indexChar2 = indexDict.get(ciphertext[k+1])

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
      print("Se presento un error")

  return cleartext



# test bench
ciphertext = encrypt("YoanPinzon", "TELL ME, O MUSE, of that ingenious hero who traveled far and wide after he had sacked the famous town of Troy")
cleartext = decrypt("YoanPinzon", ciphertext)
