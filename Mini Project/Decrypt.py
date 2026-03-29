import random
import string

def decryp_text(encrypted_text, shift):
    cleaned_list = []
    for char in encrypted_text:
        if char.isalpha():
            cleaned_list.append(char)
    
    cleaned_text = ''.join(cleaned_list)

    decrypted = []

    for char in cleaned_text:
        if char.isalpha():
            if char.isupper():
                startAscval = ord("A")
            else:
                startAscval = ord("a")
            shifted = chr(startAscval + (ord(char) - startAscval - shift) %26 )
            decrypted.append(shifted)
    decrypted_text = ''.join(decrypted)
    return decrypted_text

encrypted_text = input("Enter the encrypted text: ")
shift = int(input("Enter the shift value: "))

decrypted_text = decryp_text(encrypted_text, shift)
print("Decrypted text: ", decrypted_text)



