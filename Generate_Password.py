import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%^&*/\?"

print()

result = lower + upper + numbers + symbols
length_of_password = 8

password = "".join(random.sample(result, length_of_password))
print("Generated Password : ",password)