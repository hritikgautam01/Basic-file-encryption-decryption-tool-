# def function_decrypt(encrypted_text):
#     decrypted_list = []
#     shift = 3  # Same shift value as encryption
#     # Remove random symbols and keep only actual characters
#     filtered_text = encrypted_text[1::2]  # Take every second character starting from the second one
    
#     for char in filtered_text:
#         if char.isalnum():
#             if char.isupper():
#                 startingAscValue = ord("A")
#                 original_char = chr((ord(char) - startingAscValue - shift) % 26 + startingAscValue)
#             elif char.isdigit():
#                 startingAscValue = ord("0")
#                 original_char = chr((ord(char) - startingAscValue - shift) % 10 + startingAscValue)
#             else:
#                 startingAscValue = ord("a")
#                 original_char = chr((ord(char) - startingAscValue - shift) % 26 + startingAscValue)
#             decrypted_list.append(original_char)
#         else:
#             decrypted_list.append(char)
#     return ''.join(decrypted_list)


# # Test the decryption function
# encrypted_text = input("Enter the encrypted text: ")
# decrypted_text = function_decrypt(encrypted_text)
# print("Decrypted text:", decrypted_text)



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


# Get the file name from the user
file_name = input("Enter the name of the file to decrypt (with extension): ")
function_decrypt_file(file_name)
