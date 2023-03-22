# created by Jaden Despeines, jdespeines@ufl.edu
# 8 digit integer password encoder


def encode_string(s):
    encode = ""
    for char in s:
        if int(char) + 3 > 9:
            # encodes digits 7-9
            encode = encode + str(int(char) - 7)
        else:
            # encodes digits 0-6
            encode = encode + str(int(char) + 3)
    return encode


def decode_string(s):
    d = ""
    # code goes here ;)
    return d


def main():
    while True:
        print(f"Menu\n" + "-"*13 + "\n1. Encode\n2. Decode\n3. Quit")
        menu_option = input("Please enter an option: ")

        if menu_option == "1":
            # encoder menu option
            password = input("Please enter your password to encode: ")
            e_pword = encode_string(password)
            print("Your password has been encoded and stored!")
        if menu_option == "2":
            # decoder menu option which uses e_pword and decode_string(s)
            continue
        if menu_option == "3":
            # break to quit program
            break
    quit()


if __name__ == '__main__':
    main()
