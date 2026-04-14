import pyDes, cv2, base64

def display_image(img):
   cv2.imshow("Image", img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()

def des_encrypt_data(key, iv, data):
    des = pyDes.des(key, mode=pyDes.CBC, IV=iv, pad=None, padmode=pyDes.PAD_PKCS5)
    ciphertext = des.encrypt(data, pad=None, padmode=pyDes.PAD_PKCS5)
    return ciphertext

def des_decrypt_data(key, iv, ciphertext):
    des = pyDes.des(key, mode=pyDes.CBC, IV=iv, pad=None, padmode=pyDes.PAD_PKCS5)
    cleartext = des.decrypt(ciphertext, pad=None, padmode=pyDes.PAD_PKCS5)
    return cleartext

if __name__ == "__main__":
    key = "JuanLuis"
    iv = "Arteaga "

    # show image
    image_path = "PICT4219.JPG"
    display_image(cv2.imread(image_path))

    # encrypt
    # open image
    with open('PICT4219.JPG', 'rb') as file:
        image = file.read()
    # encrypt the image
    ciphertext = des_encrypt_data(key, iv, image)
    # encode in base64
    ciphertext_b64 = base64.standard_b64encode(ciphertext)

    print("Mensaje cifrade en Base64")
    print(ciphertext_b64)

    # decryption
    # decode
    ciphertext2 = base64.standard_b64decode(ciphertext_b64)
    # decrypt
    cleartext2 = des_decrypt_data(key, iv, ciphertext2)
    # save to image
    with open('PICT4219(1).JPG', 'wb') as file:
        file.write(cleartext2)
    display_image(cv2.imread('PICT4219(1).JPG'))

    cleartext = "Texto a ser encriptado"
    des = pyDes.des(key, mode=pyDes.CBC, IV=iv, pad=None, padmode=pyDes.PAD_PKCS5)
    ciphertext = des.encrypt(cleartext, pad=None, padmode=pyDes.PAD_PKCS5)
    decrypted = des.decrypt(ciphertext, pad=None, padmode=pyDes.PAD_PKCS5)
    print("Ciphertext is: ", ciphertext)
    print("The decrypted text is: ", decrypted)

