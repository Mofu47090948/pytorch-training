from function import add

def count_word(text, target) :
    assert isinstance(text, str)
    assert isinstance(target, str)
    assert len(target) == 1
    count = 0
    for char in text:
        if char == target:
            count = add(count, 1)
            
    return count