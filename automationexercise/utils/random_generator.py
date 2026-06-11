import random

def generate_email():

    number = random.randint(
        10000,
        99999
    )

    return f"test{number}@yopmail.com"