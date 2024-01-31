# importing the random module
import random

# a function that will generate a password on length (n) and return it.


def generatePassword(chars, numbers, symbols):
    # defining the string of choices of characters, numbers, and symbols.
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "123456789"
    syms = "!@#$%^&*()"

    """
    The random.sample() method returns a list, so we need to convert it into a string before returning it.
    """

    chosenLetters = random.sample(characters, chars)
    chosenNumbers = random.sample(nums, numbers)
    chosenSymbols = random.sample(syms, symbols)

    # creating a list denoting password
    passwordList = chosenLetters + chosenNumbers + chosenSymbols

    # we need to shuffle the list so that the numbers, characters, and symbols get shuffled
    random.shuffle(passwordList)

    # finally converting the list into string
    password = "".join(passwordList)

    return password


if __name__ == "__main__":

    chars = int(
        input("Enter the number of the character that you want in your password:"))
    numbers = int(
        input("Enter the number of the numbers that you want in your password: "))
    symbols = int(
        input("Enter the number of the symbols that you want in your password: "))

    password = generatePassword(chars, numbers, symbols)
    print("A randomly selected password is:", password)
