import random
import string
print(f"This program is designed for Random password Generation of any length")
while True:
    length = int(input(f"Enter the length for password ---> "))
    if length == 0 :
        print(f"Zero length is not allowed try again ")
    else :
        character = (string.ascii_letters) + (string.digits)
        password = ''.join(random.choice(character) for i in range(length))
        break
print(f"Random generated password of lenght {length} is ---> {password}")
