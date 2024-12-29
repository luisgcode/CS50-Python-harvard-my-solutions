def system():
    question = input("Greeting: ").lower().strip()

    if question == "hello" or question.startswith("hello"):
        print("$0")
    elif question.startswith("h", 0, 1):
        print("$20")
    else:
        print("$100")




system()
