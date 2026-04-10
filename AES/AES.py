import os, pyaes, cv2, base64, numpy as np

def reduce_image_size(input_file, factor, output_file):
   # load image and reduced its size
   img = cv2.imread(input_file)
   small = cv2.resize(img, None, fx=factor, fy=factor, interpolation=cv2.INTER_AREA)
   cv2.imwrite(output_file, small)

def display_image(img):
   cv2.imshow("Image", img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()

def convert_bytes_to_image(data):
   img_arr = np.frombuffer(data, np.uint8)
   img_decoded = cv2.imdecode(img_arr, cv2.IMREAD_UNCHANGED)
   if img_decoded is None:
    raise ValueError("Image decoding failed")
   return img_decoded

def aes_encrypt_file(key, iv, img_path):
   aes = pyaes.AESModeOfOperationOFB(key, iv) # no size restrictions for cleartext

   # load image bytes to cleartext
   with open(img_path, "rb") as f:
      cleartext = f.read()

   ciphertext = aes.encrypt(cleartext)
   return ciphertext

def aes_decrypt(key, iv, data):
   aes = pyaes.AESModeOfOperationOFB(key, iv) # no size restrictions for cleartext
   decrypted = aes.decrypt(data)
   return decrypted

if __name__ == "__main__":
   key_128 = os.urandom(16)
   iv = os.urandom(16)

   image_path = "PICT4169.JPG"
   enc_file_path = "file.txt"

   # show image
   display_image(cv2.imread(image_path))

   #encrypt
   ciphertext = aes_encrypt_file(key_128, iv, image_path)

   # save to file
   ciphertext_b64 = base64.standard_b64encode(ciphertext)
   with open(enc_file_path, "wb") as f:
      f.write(ciphertext_b64)
   print("Image saved to", enc_file_path)
   print("Printing Base64")
   print(ciphertext_b64)

   # open file backl
   with open(enc_file_path, "rb") as f:
      ciphertext_b64 = f.read()

   # decode from base64
   ciphertext = base64.standard_b64decode(ciphertext_b64)

   decrypted = aes_decrypt(key_128, iv, ciphertext)

   print("Displaying image")
   display_image(convert_bytes_to_image(decrypted))

   # TEST2
   key_192 = os.urandom(24)
   iv = os.urandom(16)

   image_path2 = "pinkamena_diane_pie.png"
   enc_file_path2 = "file2.txt"

   # show image
   display_image(cv2.imread(image_path2))

   ciphertext = aes_encrypt_file(key_192, iv, image_path2)

   # save to file
   ciphertext_b64 = base64.standard_b64encode(ciphertext)
   with open(enc_file_path2, "wb") as f:
      f.write(ciphertext_b64)
   print("Image saved to", enc_file_path2)
   print("Printing Base64")
   print(ciphertext_b64)

   # open file backl
   with open(enc_file_path2, "rb") as f:
      ciphertext_b64 = f.read()

   # decode from base64
   ciphertext = base64.standard_b64decode(ciphertext_b64)

   decrypted = aes_decrypt(key_192, iv, ciphertext)

   print("Displaying 2nd image")
   display_image(convert_bytes_to_image(decrypted))
