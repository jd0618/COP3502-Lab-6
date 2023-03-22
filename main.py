# created by Jaden Despeines, jdespeines@ufl.edu
# decoder by Kyle Weiner kyleweiner@ufl.edu
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


def decode(encode):
    password = ''
    for digit in encode:
        decoded_digit = str((int(digit) - 3) % 10)
        password += decoded_digit
    return password


def main():
    while True:
        print(f"Menu\n" + "-"*13 + "\n1. Encode\n2. Decode\n3. Quit")
        menu_option = input("Please enter an option: ")

        if menu_option == "1":
            # encoder menu option
            password = input("Please enter your password to encode: ")
            encode = encode_string(password)
            print("Your password has been encoded and stored!")
        if menu_option == "2":
            password = decode(encode)
            print(f"The encoded password is {encode}, and the original password is {password}.")
        if menu_option == "3":
            # break to quit program
            break
    quit()


if __name__ == '__main__':
    main()
