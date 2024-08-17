import textwrap

def main():
    prompt("Enter a number:")
    x = float(input())
    prompt("Enter another number:")
    y = float(input())
    instruction = textwrap.dedent("""Choose one of:
    1) add (a)
    2) subtract (s)
    3) multiply (m)
    4) divide (d)
        """)
    prompt(instruction)
    operation = input()

    while True:

        match operation:
            case "add" | "a" | "1":
                return x + y
            case "subtract" | "s" | "2":
                return x - y
            case "multiply" | "m" | "3":
                return x * y
            case "divide" | "d" | "4":
                return x / y
            case _:
                prompt(f"Operation '{operation}' invalid. {instruction}")
                operation = input()

def prompt(message):
    print(f"==> {message}")

if __name__ == "__main__":
    print(main())
