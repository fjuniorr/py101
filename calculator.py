import textwrap

def main():
    x = float(input("Enter a number:"))
    y = float(input("Enter another number:"))
    instruction = textwrap.dedent("""Choose one of:
    - add (a)
    - subtract (s)
    - multiply (m)
    - divide (d)
        """)
    operation = input(instruction)

    while True:

        match operation:
            case "add" | "a":
                return x + y
            case "subtract" | "s":
                return x - y
            case "multiply" | "m":
                return x * y
            case "divide" | "d":
                return x / y
            case _:
                operation = input("Operation invalid. "+ instruction)

if __name__ == "__main__":
    print(main())
