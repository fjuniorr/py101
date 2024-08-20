## Answer

```python
MESSAGES = {
    "hello": "Welcome to Calculator!",
    "first_number": "What's the first number?",
    "second_number": "What's the second number?",
    "invalid_number": "Hmm... that doesn't look like a valid number.",
    "operation_picker": "What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide",
    "invalid_operation_picker": "You must choose 1, 2, 3, or 4",
    "keep_going": "Do you want to perform another calculation? Type yes or no.",
    "invalid_keep_going": "Type yes or no.",
    "result": "The result is"
}

def main():
    prompt(MESSAGES["hello"])
    calculator()
    while keep_going():
        calculator()

def calculator():
    prompt(MESSAGES["first_number"])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES["invalid_number"])
        number1 = input()

    prompt(MESSAGES["second_number"])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES["invalid_number"])
        number2 = input()

    prompt(MESSAGES["operation_picker"])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(MESSAGES["invalid_operation_picker"])
        operation = input()

    match operation:
        case "1":
            output = int(number1) + int(number2)
        case "2":
            output = int(number1) - int(number2)
        case "3":
            output = int(number1) * int(number2)
        case "4":
            output = int(number1) / int(number2)

    prompt(f"{MESSAGES['result']} {output}")

def keep_going():
    prompt(MESSAGES["keep_going"])
    result = None
    repeat = input()
    while result is None:
        match repeat.lower():
            case "yes" | "y":
                result = True
            case "no" | "n":
                result = False
            case _:
                prompt(MESSAGES["invalid_keep_going"])
    return result

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

main()
```
