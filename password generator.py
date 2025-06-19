import random
import string

def generate_password ():
    print("=== Password Generate ===")

    length = int(input(" Enter desired Password length: "))

    use_lowercase = input("Include all lowercase ? (y/n): ").lower() == "y"
    use_uppercase = input("Include all uppercase? (y/n): ").lower() == "y"
    use_digit = input("include digit? (y/n):").lower() == "y"
    use_special = input("Include special character ?(y/n):").lower() == "y" 

    characters =""

    if use_uppercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digit:
        characters +=string.digits
    if use_special:
        characters +=string. punctuation
    if not characters:
        print("you must select at least one charcter set!")
        return characters
    password = " ".join(random.choice(characters) for  _ in range(length))
    print("generated password:", password)
generate_password()
