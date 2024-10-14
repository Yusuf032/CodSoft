import random
import string

length = int(input("Enter Length"))

chars = string.ascii_letters
chars += string.digits
chars +=  string.punctuation

password = [random.choice(chars) for i in range(length)]

print("Here is your Random Password:",password)
