from cryptography.fernet import Fernet
message = "hello geeks"
key = Fernet.generate_key()
fernet = Fernet(key)
encmessage = fernet.encrypt(message.encode())

print("original", message)
print("encrypted", encmessage)

decMessage = fernet.decrypt(encmessage).decode()
print("decrypted string",decMessage)

