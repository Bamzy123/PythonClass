def caesar_decrypt(ciphertext, shift):

	decrypted_text = ""

	for char in ciphertext:
		if char.isupper():
			decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
		elif char.islower():
			decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
		else:
			decrypted_text += char
	return decrypted_text

def caesar_encrypt(plaintext, shift):

	encrypted_text = ""

	for char in plaintext:
		if char.isupper():
			encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
		elif char.islower():
			encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
		else:
			encrypted_text += char
	return encrypted_text


print("Welcome to Caesar Cipher!")
choice = input("Do you want to(E)ncrypt or (D)erypt? ").strip().upper()

if choice in ['E', 'D']:
	message = input("Enter your message: ").strip()
	shift = int(input("Enter the shift value (0-25): ").strip())

	if 0 <= shift <= 25:
		if choice == 'E':
			result = caesar_encrypt(message, shift)
			print("Encrypted Message: ", result)
		else:
			result = caesar_decrypt(message, shift)
			print("Decrypted Message: ", result)

	else:
		print("Error: shift value must be between 0 and 25...")

else:
	print("Error: Invalid choice, please enter 'E' for encrypt or 'D' for decrypt...")