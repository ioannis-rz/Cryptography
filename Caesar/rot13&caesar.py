import string

class Caesar:
  def __init__(self, key):
    self.key = key

  def encrypt(self, cleartext):
    cleartext = cleartext.lower().replace(" ","")
    cyphertext = []
    for char in cleartext:
      temp = ((ord(char) + self.key) % 123)
      if temp < 97:
        temp += 97
      cyphertext.append(chr(temp))
    return ''.join(cyphertext)

  def decrypt(self, cyphertext):
    cyphertext = cyphertext.lower().replace(" ","")
    cleartext = []
    for char in cyphertext:
      temp = ((ord(char) - self.key))
      if temp < 97:
        temp += 26
      cleartext.append(chr(temp))
    return ''.join(cleartext)

cipher = Caesar(4)
test = cipher.encrypt("see you in two long weeks")
print(test)
test = cipher.decrypt(test)
print(test)
