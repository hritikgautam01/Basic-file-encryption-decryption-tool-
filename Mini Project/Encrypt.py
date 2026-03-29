import random
import string

def encrypt_text(text, shift):
    encrypted = []
    for char in text:
        if char.isalpha():
            if char.isupper():
                startingAscval = ord("A")
            else:
                startingAscval = ord("a")
            shifted = chr((startingAscval) + ((ord(char) - startingAscval + shift) % 26))
            encrypted.append(shifted)
        else:
            encrypted.append(char)

    encrypted_text = ''.join(encrypted)
    final_encrypted = ""
    for i in encrypted_text:
        random_symbol = random.choice(['@', '$', '*', '^', '&', '#'])
        final_encrypted += random_symbol + char 
    return final_encrypted

text = input("Enter text to encrypt: ")
shift = int(input("Enter shift value (e.g., 3): "))

encrypted_text = encrypt_text(text,shift)
print("Encrypted text: ", encrypted_text)






