# after reading I got: 
# You may assume that both list arguments have the same number of elements.

def main(numbers1: list, numbers2: list) -> list:
    """
    Returns merged list where: 
    - even indexes are filled with numbers1;
    - odd indexes are filled with numbers2.

    for i=0 in length of bigger list:
        if there are still elements in numbers1:
            insert at i
        if there are still elements in numbers2:
            insert at i+1
    """
    result = []
    length = len(numbers1) if len(numbers1) > len(numbers2) else len(numbers2)
    for _ in range(length):
        if numbers1:
            result.append(numbers1.pop(0))
        else:
            result.append(None)
        if numbers2:
            result.append(numbers2.pop(0))
        else:
            result.append(None)
    return result

def test_main():
    assert main([12, 14], [13, 15, 17]) == [12, 13, 14, 15, None, 17]
