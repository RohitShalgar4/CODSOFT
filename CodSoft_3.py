import random
import string

def gen_pass(len):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(len))
    return password


def main():
    print("Password Generator")
    while True:
        try:
            len = int(input("Length of the password to be (in numbers):"))
            if len <= 0:
                raise ValueError("ENter a positive number.")
            break
        except ValueError:
            print("Error. Error a valid number.")
    password = gen_pass(len)
    print(f"Your generated password is :{password}")

if __name__ == "__main__":
    main()