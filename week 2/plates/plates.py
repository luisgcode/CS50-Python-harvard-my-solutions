def main():
    plate = input("Plate: ").casefold().strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    valid_letter = ["a","c","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    valid_number = ["0", "1","2","3","4","5","6","7","8","9"]

    if not s.isalnum():
        return False
    elif s.isalpha() and len(s) > 2 and len(s) <= 6:
        return True
    elif len(s) <=2:
        return False
    elif len(s) == 3 and s[0] in valid_letter and s[1] in valid_letter and s[-1] in valid_number:
        return True
    elif len(s) == 4 and s[0] in valid_letter and s[1] in valid_letter and s[-1] in valid_number and s[-2] in valid_number and s[-2] != "0":
        return True
    elif len(s) == 5 and s[0] in valid_letter and s[1] in valid_letter and s[-1] in valid_number and s[-2] in valid_number and s[-3] != "0":
        return True
    elif len(s) == 6 and s[0] in valid_letter and s[1] in valid_letter and s[-1] in valid_number and s[-2] in valid_number and s[-4] != "0":
        return True
    else:
        return False

main()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ “All vanity plates must start with at least two letters.”
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable vanity plate; AAA22A would not be acceptable.
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ The first number used cannot be a ‘0’.”
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ “No periods, spaces, or punctuation marks are allowed.”


