def main():
    convert(input(""))

def convert(str):
    if str == "Hello :)":
        print("Hello 🙂")
    elif str == "Goodbye :(":
        print("Goodbye 🙁")
    elif str == "Hello :) Goodbye :(":
        print("Hello 🙂 Goodbye 🙁")
    else:
        print(str)
    return str


main()
