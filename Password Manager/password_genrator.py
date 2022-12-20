import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_passwords = [random.choice(letters) for _ in range(random.randint(6, 8))]
    number_passwords = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    symbol_passwords = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = letter_passwords + number_passwords + symbol_passwords

    random.shuffle(password_list)

    password = "".join(password_list)

    return password

