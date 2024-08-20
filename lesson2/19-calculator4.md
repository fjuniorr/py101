## Answer

```python
LANG = "pt"
# os.getenv("LANG")[0:2] 
# locale.getdefaultlocale()[0][0:2]
MESSAGES = {
    "hello": 
        {
            "en": "Welcome to Calculator!",
            "pt": "Bem vindo a Calculadora!"
        },
    "first_number": 
        {
            "en": "What's the first number?",
            "pt": "Digite o primeiro número"
        },
    "second_number": 
        {
            "en": "What's the second number?",
            "pt": ""
        },
    "invalid_number": 
        {
            "en": "Hmm... that doesn't look like a valid number.",
            "pt": ""
        },
    "operation_picker": 
        {
            "en": "What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide",
            "pt": ""
        },
    "invalid_operation_picker": 
        {
            "en": "You must choose 1, 2, 3, or 4",
            "pt": ""
        },
    "keep_going": 
        {
            "en": "Do you want to perform another calculation? Type yes or no.",
            "pt": ""
        },
    "invalid_keep_going": 
        {
            "en": "Type yes or no.",
            "pt": ""
        },
    "result": 
        {
            "en": "The result is",
            "pt": ""
        }
}

def main():
    prompt(messages("hello", LANG))
    calculator()
    while keep_going():
        calculator()

def messages(slug, lang=None):
    default = MESSAGES[slug]["en"]
    return MESSAGES[slug].get(lang) or default

def calculator():
    prompt(messages("first_number", LANG))
    number1 = input()

    while invalid_number(number1):
        prompt(messages("invalid_number", LANG))
        number1 = input()

    prompt(messages("second_number", LANG))
    number2 = input()

    while invalid_number(number2):
        prompt(messages("invalid_number", LANG))
        number2 = input()

    prompt(messages("operation_picker", LANG))
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(messages("invalid_operation_picker", LANG))
        operation = input()

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    prompt(f"{messages('result', LANG)} {output}")

def keep_going():
    prompt(messages("keep_going"))
    result = None
    repeat = input()
    while result is None:
        match repeat.lower():
            case "yes" | "y":
                result = True
            case "no" | "n":
                result = False
            case _:
                prompt(messages("invalid_keep_going", LANG))
    return result

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

main()
```

## Reflection

I forgot to convert `float` in the match block. My approach in `09-calculator.py` was better.
