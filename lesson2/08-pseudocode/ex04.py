def main(char, string) -> int:
    """Returns index of 3rd occurrence of char in string

    initialize count of occurrences
    for each current_char in string
        if current_char == char
            increment count of occurrence
            if count of occurence == 3
                return index
    """
    count = 0
    for index, current_char in enumerate(string):
        if current_char == char:
            count += 1
            if count == 3:
                return index

print(main("x", "axbxcdxex"))
print(main("x", "axbxcdeß"))
