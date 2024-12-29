def main():
    # Prompt the user for a camelCase variable
    camel_case = input("camelCase: ")

    # Convert the camelCase input to snake_case
    snake_case = camel_to_snake(camel_case)

    # Output the result
    print("snake_case:", snake_case)


def camel_to_snake(camel_case):
    # Initialize an empty string to store the snake_case result
    snake_case = ""

    # Loop through each character in the camelCase string
    for char in camel_case:
        if char.isupper():  # Check if the character is uppercase
            snake_case += "_" + char.lower()  # Add underscore and convert to lowercase
        else:
            snake_case += char  # Add the character as is

    return snake_case


# Run the program
main()
