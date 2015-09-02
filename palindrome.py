def is_palindrome(sentence):
    pal = []
    for x in sentence:
        if x.isalnum() == True:
            pal.append(x.lower())
        else:
            pass
    if pal[:] == pal[-1::-1]:
        return True
    else:
        return False


def main():
    name = input("Please enter a word or sentence > ")
    print(is_palindrome(name))

if __name__ == '__main__':
    main()
