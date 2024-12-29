def main():
    question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

    if question == '42':
        positive()
    elif question == 'forty two':
        positive()
    elif question == 'forty-two':
        positive()
    else:
        negative()


def positive():
    print("Yes")

def negative():
    print("No")

main()
