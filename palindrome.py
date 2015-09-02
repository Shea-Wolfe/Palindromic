import re
# def is_palindrome(sentence):
#     pal = []
#     for x in sentence:
#         if x.isalnum() == True:
#             pal.append(x.lower())
#         else:
#             pass
#     if pal[:] == pal[-1::-1]:
#         return True
#     else:
#         return False
# def is_palindrome(sentence):
#     thing = re.sub(r'[^A-Za-z]',"",sentence).lower()
#     if len(thing) <=1:
#         return True
#     else:
#         if thing[0] == thing[-1]:
#             return is_palindrome(thing[1:-1])
#         else:
#             return False
def is_palindrome(sentence):
    thing = re.sub(r'[^A-Za-z]',"",sentence).lower()
    count = 0
    test = []
    for x in thing:
        if x == thing[-1-count]:
            count += 1
        else:
            pass
    if count == len(thing):
        return True
    else:
        return False

def main():
    name = input("Please enter a word or sentence > ")
    print(is_palindrome(name))

if __name__ == '__main__':
    main()

x, y = (1,2)
