def random_password_genorator():
    import random
    import string

    length = int(input("Enter your desired passwrod length: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    print(f"Your password is: {password}")

random_password_genorator()