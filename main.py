import string
import random   

alphabet = string.ascii_letters + string.digits + string.punctuation
pass_len = int(input("How long do you want your password to be: "))
try:
    a=int(pass_len)
except ValueError:
    print(f"{pass_len} is not a number. Enter a number: ")

    


def generate_password():
    password = ''.join(random.choices(alphabet, k=pass_len))
    return password

new_password = generate_password
print("This is your password: " + generate_password())



    