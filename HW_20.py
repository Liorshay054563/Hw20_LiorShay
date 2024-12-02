# start === HW_20
# 1

def brackets(word: str):
    """find if the brackets is valid"""
    open_bracket_list = []
    for i in word:
        if i in ['{','[','(']:
            open_bracket_list.append(i)
            continue
        if i in ['}',']',')']:
            if len(open_bracket_list) == 0:
                return False
            last = open_bracket_list[-1]
            if i == "}" and last == "}" or i == ']' and last == '[' or i == ')' and last == '(':
                open_bracket_list.pop()
        else:
            return False
    if len(open_bracket_list) == 0:
        return True
    else:
        return False





# 2

def remove_dup(numbers: list[int]) -> None:
    """remove duplicite numbers from the list"""
    index = 1
    while index < len(numbers):
        if numbers[index] == numbers[index - 1]:
            numbers.pop(index)
        else:
            index += 1

numbers: list[int] = [1, 1, 2, 2, 2, 2, 3, 4, 5, 6, 7, 7, 8]
remove_dup(numbers)
print(numbers)





# 3
def united_and_sorted(x: list[int], y: list[int]):
    """return 1 sorted list from 2 listewaew    """
    l_united: list[int] = x + y
    l_uni_sort = []

    while l_united:
        min_num = min(l_united)
        l_uni_sort.append(min_num)
        l_united.remove(min_num)
    return l_uni_sort


print(united_and_sorted([1,2,4],[1,3,4]))






