def is_palindrome(sentence):
    if sentence[:] == sentence[-1::-1]:
        return "That's a Palindrome!"
    return "That's not a Palindrome!"


def main():
    name = input("Please enter a word or sentence > ")
    print(is_palindrome(name))

if __name__ == '__main__':
    main()
