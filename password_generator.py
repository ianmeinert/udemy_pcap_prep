import random
import string


def length_input():
    length = input("Provide password length: ")

    if length.isdigit():
        return int(length)
    else:
        print("Invalid response")
        return length_input()


def include_option_input(str):
    resp = input(f"Use {str}? (y/n): ").lower()

    if resp in ["y", "n"]:
        return resp == "y"
    else:
        print("Invalid response")
        return include_option_input(str)


def generate_string(char_str=None, sample_size=1):
    char_list = list(char_str) if char_str is not None else list(string.ascii_lowercase)
    random.shuffle(char_list)

    return "".join(random.sample(char_list, sample_size))


def generate_password():
    chars_str = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    digits = "".join([str(i) for i in range(10)])
    spcl_chars = string.punctuation

    length = length_input()
    do_incl_upper = include_option_input("uppercase letters")
    do_incl_digits = include_option_input("digits")
    do_incl_spcl = include_option_input("special characters")

    if do_incl_upper:
        chars_str += upper_chars

    if do_incl_digits:
        chars_str += digits

    if do_incl_spcl:
        chars_str += spcl_chars

    pw = generate_string(char_str=chars_str, l=length)

    print("\nGenerated password: ", pw, "\n")


def main():
    menu = """-- Password generator --
    Choose option:
    1: generate password
    2: exit the program
    Your choice: """

    res = input(menu)

    match res:
        case "1":
            generate_password()
        case "2":
            print("Bye!")
            quit()
        case _:
            print("Please enter a correct value")

    main()


main()
