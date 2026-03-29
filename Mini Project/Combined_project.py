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





def function_decrypt_file(file_name):
    try:
        # Read the encrypted contents of the file
        with open(file_name, 'r') as file:
            encrypted_text = file.read()

        # Remove random symbols and keep only actual characters
        filtered_text = encrypted_text[1::2]  # Take every second character starting from the second one
        
        # Perform decryption (reverse of encryption logic)
        decrypted_list = []
        shift = 3  # Same shift value as encryption
        for char in filtered_text:
            if char.isalnum():
                if char.isupper():
                    startingAscValue = ord("A")
                    original_char = chr((ord(char) - startingAscValue - shift) % 26 + startingAscValue)
                elif char.isdigit():
                    startingAscValue = ord("0")
                    original_char = chr((ord(char) - startingAscValue - shift) % 10 + startingAscValue)
                else:
                    startingAscValue = ord("a")
                    original_char = chr((ord(char) - startingAscValue - shift) % 26 + startingAscValue)
                decrypted_list.append(original_char)
            else:
                decrypted_list.append(char)

        decrypted_text = ''.join(decrypted_list)

        # Save the decrypted text to a new file
        output_path = "decrypted_text.txt"  # Output fixed to current directory
        with open(output_path, 'w') as output_file:
            output_file.write(decrypted_text)

        print(f"Decryption successful! Decrypted text saved to: {output_path}")
    
    except FileNotFoundError:
        print("Error: The file was not found. Please check the file name.")
    except Exception as e:
        print(f"An error occurred: {e}")



print("Choose an option: ")
print("1.Encrypt Text")
print('2-Decrypt Text')
choice = int(input("Enter the number: "))

if choice == 1:
    file_path = input("Enter the path of the file to encrypt: ")
    function_encrypt_file(file_path)

elif choice == 2:
    file_name = input("Enter the name of the file to decrypt (with extension): ")
    function_decrypt_file(file_name)

else:
    print("Enter a Valid number")