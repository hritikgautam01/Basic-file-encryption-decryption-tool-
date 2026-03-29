# import random
# import os 


# def function_encrypt(text):
#     list_1 = []
#     shift = 3  # Define the shift value explicitly
#     for char in text:
#         if char.isalnum():
#             if char.isupper():
#                 startingAscValue = ord("A")
#                 shifted_char = chr((ord(char) - startingAscValue + shift) % 26 + startingAscValue)
#             elif char.isdigit():
#                 startingAscValue = ord("0")
#                 shifted_char = chr((ord(char) - startingAscValue + shift) % 10 + startingAscValue)
#             else:
#                 startingAscValue = ord("a")
#                 shifted_char = chr((ord(char) - startingAscValue + shift) % 26 + startingAscValue)
#             list_1.append(shifted_char)
#         else:
#             list_1.append(char)
#     Join_txt = ''.join(list_1)
    
#     # Add random symbols between each character
#     Encrypted_txt = ""
#     for i in Join_txt:
#         random_symbol = random.choice(['@', '$', '*', '^', '&', '#'])
#         Encrypted_txt += random_symbol + i
#     return Encrypted_txt

# text = input("Enter the text: ")
# m = function_encrypt(text)
# print(m)





import random
import os

def function_encrypt_file(file_path):
    try:
        # Read the contents of the file
        with open(file_path, 'r') as file:
            text = file.read()

        # Perform encryption (same logic as before)
        list_1 = []
        shift = 3  # Define the shift value explicitly
        for char in text:
            if char.isalnum():
                if char.isupper():
                    startingAscValue = ord("A")
                    shifted_char = chr((ord(char) - startingAscValue + shift) % 26 + startingAscValue)
                elif char.isdigit():
                    startingAscValue = ord("0")
                    shifted_char = chr((ord(char) - startingAscValue + shift) % 10 + startingAscValue)
                else:
                    startingAscValue = ord("a")
                    shifted_char = chr((ord(char) - startingAscValue + shift) % 26 + startingAscValue)
                list_1.append(shifted_char)
            else:
                list_1.append(char)
        Join_txt = ''.join(list_1)

        # Add random symbols between each character
        Encrypted_txt = ""
        for i in Join_txt:
            random_symbol = random.choice(['@', '$', '*', '^', '&', '#'])
            Encrypted_txt += random_symbol + i

        # Save the encrypted text to a new file
        output_path = os.path.join(os.path.dirname(file_path), "encrypted_text.txt")
        with open(output_path, 'w') as output_file:
            output_file.write(Encrypted_txt)

        print(f"Encryption successful! Encrypted text saved to: {output_path}")
    
    except FileNotFoundError:
        print("Error: The file was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Get the file path from the user
file_path = input("Enter the path of the file to encrypt: ")
function_encrypt_file(file_path)
