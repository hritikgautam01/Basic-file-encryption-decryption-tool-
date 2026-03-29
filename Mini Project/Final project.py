import random
import os 

def function_encrypt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()

        list_1 = []
        shift = 3
        for char in text:
            if char.isalnum():
                if char.isupper():
                    startingAscVal = ord("A")
                    shifted_char = chr((ord(char) - startingAscVal + shift)%26 + startingAscVal)
                elif char.isdigit():
                    startingAscVal = ord(0)
                    shifted_char = chr((ord(char) - startingAscVal + shift)%10 + startingAscVal )
                else:
                    startingAscVal = ord('a')
                    shifted_char = chr((ord(char) - startingAscVal + shift)%26 + startingAscVal)
                list_1.append(shifted_char)
            else:
                list_1.append(char)
        Join_text = ''.join(list_1)

        #Adding random symbols after each encryption
        Encrypted_txt = ""
        for i in Join_text:
            random_symbol = random.choice(['@', '$', '*', '^', '&', '#'])
            
            Encrypted_txt += random_symbol + i
        

        output_file = "encrypted_text.txt"
        with open(output_file, 'w') as file:
            file.write(Encrypted_txt)

        print('Encryption successful!')
    
    except FileNotFoundError:
        print("Error: The file was not found. Please enter the correct path")
    except Exception as e:
        print(f'An error occured: {e}')


def function_decrypt_file(file_name):
    try:
        with open(file_name, 'r') as file:
            encrypted_text = file.read()

        filtered_text = encrypted_text[1::2]

        decrypted_list = []
        shift = 3
        for char in filtered_text:
            if char.isalnum():
                if char.isupper():
                    startingAscValue = ord("A")
                    original_char = chr((ord(char) - startingAscValue - shift) %26 + startingAscValue)
                elif char.isdigit():
                    startingAscValue = ord(0)
                    original_char = chr((ord(char) - startingAscValue - shift)%10 + startingAscValue)
                else:
                    startingAscValue = ord("a")
                    original_char = chr((ord(char) - startingAscValue - shift) %26 + startingAscValue)
                decrypted_list.append(original_char)
            else:
                decrypted_list.append(char)
        
        decrypted_text = ''.join(decrypted_list)

        output_file = "decrypted_text.txt"
        with open(output_file,"w") as file:
            file.write(decrypted_text)

        print("Decryption successful!")
    except FileNotFoundError:
        print("Error: The file was not found. Please check the file name.")
    except Exception as e:
        print(f"An error occured: {e}")


print("Choose an option: ")
print("1 - Encrypt text")
print("2 - Decrypt file")
choice = int(input("Enter the number: "))

if choice == 1:
    file_path = input("Enter the path of the file to encrypt: ")
    function_encrypt_file(file_path)
elif choice == 2:
    file_name = input("Enter the file name with path: ")
    function_decrypt_file(file_name)
else:
    print("Choose a valid option")