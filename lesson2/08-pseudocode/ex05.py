from itertools import zip_longest

def main(numbers1: list, numbers2: list) -> list:
    result = []
    for pair in zip_longest(numbers1, numbers2):
        result.extend(pair)
    return result

def test_main():
    assert main([12, 14], [13, 15, 17]) == [12, 13, 14, 15, None, 17]
