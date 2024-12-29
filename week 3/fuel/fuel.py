def main():
    convertion()


def convertion():
    while True:
        try:
            fraction = input("Insert your fraction: ").split('/')
            n1 = int(fraction[0])
            n2 = int(fraction[1])

        except ValueError:
            print("Not valid format")
        except ZeroDivisionError:
            print("Not valid format")

        else:
            if n1 == 0 and n2 == 100 or n1 == 1 and n2 == 100 or n1 == 0 and n2 == 4:
                print("E")
                break
            elif n1 == 100 and n2 == 100 or n1 == 99 and n2 == 100 or n1 == 4 and n2 == 4:
                print("F")
                break
            elif n1 == 1 and n2 == 2:
                print("50%")
                break
            elif n1 == 1 and n2 == 4:
                print("25%")
                break
            elif n1 == 1 and n2 == 3:
                print("33%")
                break
            elif n1 == 2 and n2 == 3:
                print("67%")
                break
            elif n1 == 3 and n2 == 4:
                print("75%")
                break

main()
