## Answer

```python
def main():
    prompt('Welcome to Calculator!')
    calculator()
    while keep_going():
        calculator()

def calculator():
    prompt("What's the first number?")
    number1 = input()

    while invalid_number(number1):
        prompt("Hmm... that doesn't look like a valid number.")
        number1 = input()

    prompt("What's the second number?")
    number2 = input()

    while invalid_number(number2):
        prompt("Hmm... that doesn't look like a valid number.")
        number2 = input()

    prompt("What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide")
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt("You must choose 1, 2, 3, or 4")
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

    prompt(f"The result is {output}")    

def keep_going():
    prompt("Do you want to perform another calculation? Type yes or no.")
    result = None
    repeat = input()
    while result is None:
        match repeat.lower():
            case "yes" | "y":
                result = True
            case "no" | "n":
                result = False
            case _:
                prompt("Type yes or no.")
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

## Solution

```python
# code omitted for brevity

while True:
    # ask for two numbers
    # ask for operation
    # perform operation and display results
    prompt('Would you like to perform another operation? (y/n) ')
    answer = input()
    if answer != 'y':
        break
```

We nest the main part of our program in a while True loop and, at the end of the loop body, we ask the user if they want to perform another calculation. If the user inputs anything other than 'y', we break out of the loop with the break statement. That looks good so far, but suppose the user enters an uppercase 'Y' or the word 'yes' instead of 'y'. What happens then? We can take care of those cases with the following change:

```python
while True:
    # code omitted for brevity

    if answer and answer[0].lower() != 'y':
        break
```

Note that we first have to check that the answer is not an empty string as trying to access an index of the empty string would raise an IndexError. Code like if answer and answer[0] is a common Python idiom for dealing with empty strings that you don't want to try indexing.

## Reflection

I did not like my `keep_going` logic to ask the user to continue. However at the end of the day I think it is better than the LS alternative because I don't have to keep the valid values both in the check

```python
while operation not in ["1", "2", "3", "4"]:
    prompt("You must choose 1, 2, 3, or 4")
    operation = input()
```

and the match statement:

```python
    match operation:
        case "1":
            output = int(number1) + int(number2)
        case "2":
            output = int(number1) - int(number2)
        case "3":
            output = int(number1) * int(number2)
        case "4":
            output = int(number1) / int(number2)
```

---

Code like `if answer and answer[0]` is a common Python idiom for dealing with empty strings that you don't want to try indexing.