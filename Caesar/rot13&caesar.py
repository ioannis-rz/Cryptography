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
for i in range(26):
  print("Iteration " + str(i))
  cipher = Caesar(i)
  test = cipher.decrypt("ns ymj nrnyfynts lfrj rtanj bmfy nx ymj sfrj ymfy fqfs yzwnsl lfaj yt ymj rfhmnsj")
  print(test)
  test = cipher.encrypt(test)
  print(test)

  # era 5 juas juas
  # Iteration 5
  # in the imitation game movie what is the name that alan turing gave to the machine

cipher = Caesar(5)
test = cipher.decrypt("fqfs")
print(test)
test = cipher.encrypt(test)
print(test)

