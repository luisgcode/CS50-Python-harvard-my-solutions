items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def program():
    bill = 0

    while True:
        try:
            item = input("Item: ").title()
            price = items[item]
            if item in items:
                bill = bill + price
                print(f"${bill:.2f}")
        except ValueError:
            pass
        except KeyError:
            pass
        except EOFError:
            break


program()


