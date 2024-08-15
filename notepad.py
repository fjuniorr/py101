import math

def print_in_box(text, width=None):
    """
    Print text inside a box
    
    If the box width is specified, text is wraped into multiple lines to fit

    Implementation:
        - split text into lines where each line has the maximum size
    """
    textline = splittext(text, width)
    textlength =  len(text) if not width else width - 4
    print(textlength)
    margin = f"+-{'-'*(textlength)}-+\n"
    padding = f"| {' '*(textlength)} |\n"
    content = [f"| {line} |\n" for line in textline]
    result = ("\n"
              + margin
              + padding
              + "".join(content)
              + padding
              + margin)
    return result

    # max_content_size = width - 4
    # lines_count = math.ceil(len(text) / max_content_size)
    # text = splittext(text, width)

def splittext(text, width):
    """
    Split text into a list os strings of size width 
    (stripping whitespaces at the end) and 
    after pad all strings to width
    """
    if len(text) < width:
        return [text]

    result = []
    index = 0
    for index in range(0, len(text)-width, width):
        result.append(text[index:index+width])
    result.append(text[index+width:-1])
    return result

example4 = """
+--------------+
|              |
| To boldly go |
| where no one |
| has gone bef |
| ore.         |
|              |
+--------------+
"""

text = "To boldly go where no one has gone before."
result = splittext(text, 12)
print(result)
expected = ['To boldly go','where no one', 'has gone bef', 'ore.        ']
assert result == expected


# print(print_in_box("To boldly go where no one has gone before.", width=16))
# print(print_in_box("To boldly go where no one has gone before."))
# assert print_in_box("To boldly go where no one has gone before.", width=16) == example4


# result = print_in_box("Way too much           whitespace!", width=28)
# expected = """
# +--------------------------+
# |                          |
# | Way too much whitespace! |
# |                          |
# +--------------------------+
# """

# assert result == expected