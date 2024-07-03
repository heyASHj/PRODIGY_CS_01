def caesar_encryption(text, shift):
    encrypted_text = ""  # Initialize an empty string to store encrypted text
    for char in text:  # Iterate through each character in the input text
        if char.isalpha():  # Check if the character is an alphabet
            shifted = ord(char) + shift  # Shift the character in ASCII value by the given shift
            if char.islower():  # If the character is lowercase
                if shifted > ord('z'):  # If shifting exceeds 'z'
                    shifted -= 26  # Wrap around to start of lowercase letters
                elif shifted < ord('a'):  # If shifting goes below 'a'
                    shifted += 26  # Wrap around to end of lowercase letters
            elif char.isupper():  # If the character is uppercase
                if shifted > ord('Z'):  # If shifting exceeds 'Z'
                    shifted -= 26  # Wrap around to start of uppercase letters
                elif shifted < ord('A'):  # If shifting goes below 'A'
                    shifted += 26  # Wrap around to end of uppercase letters
            encrypted_text += chr(shifted)  # Append the shifted character to encrypted_text
        else:  # If the character is not an alphabet (like punctuation or spaces)
            encrypted_text += char  # Just append it unchanged to encrypted_text
    return encrypted_text  # Return the fully encrypted text

def caesar_decryption(encrypted_text, shift):
    decrypted_text = ""  # Initialize an empty string to store decrypted text
    for char in encrypted_text:  # Iterate through each character in the encrypted text
        if char.isalpha():  # Check if the character is an alphabet
            shifted = ord(char) - shift  # Shift the character in ASCII value by the inverse of the encryption shift
            if char.islower():  # If the character is lowercase
                if shifted > ord('z'):  # If shifting exceeds 'z'
                    shifted -= 26  # Wrap around to start of lowercase letters
                elif shifted < ord('a'):  # If shifting goes below 'a'
                    shifted += 26  # Wrap around to end of lowercase letters
            elif char.isupper():  # If the character is uppercase
                if shifted > ord('Z'):  # If shifting exceeds 'Z'
                    shifted -= 26  # Wrap around to start of uppercase letters
                elif shifted < ord('A'):  # If shifting goes below 'A'
                    shifted += 26  # Wrap around to end of uppercase letters
            decrypted_text += chr(shifted)  # Append the shifted character to decrypted_text
        else:  # If the character is not an alphabet (like punctuation or spaces)
            decrypted_text += char  # Just append it unchanged to decrypted_text
    return decrypted_text  # Return the fully decrypted text

# Function to get user input and perform encryption or decryption
def main():
    while True:  # Loop indefinitely until user decides to stop
        choice = input("Do you want to encrypt or decrypt? (e/d): ").strip().lower()  # Prompt user for choice
        if choice not in ['e', 'd']:  # If choice is not 'e' or 'd', ask again
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
            continue
        
        text = input("Enter the text: ").strip()  # Get the text to encrypt or decrypt
        shift = int(input("Enter the shift value (1-25): ").strip())  # Get the shift value
        
        if choice == 'e':  # If user chose encryption
            encrypted_text = caesar_encryption(text, shift)  # Encrypt the text
            print("Encrypted text:", encrypted_text)  # Print the encrypted text
        elif choice == 'd':  # If user chose decryption
            decrypted_text = caesar_decryption(text, shift)  # Decrypt the text
            print("Decrypted text:", decrypted_text)  # Print the decrypted text
        
        another = input("Do you want to encrypt/decrypt another text? (y/n): ").strip().lower()  # Ask if user wants to continue
        if another != 'y':  # If user does not want to continue
            break  # Exit the loop and end the program

if __name__ == "__main__":  # If this script is run directly
    main()  # Call the main function to start the encryption/decryption process
