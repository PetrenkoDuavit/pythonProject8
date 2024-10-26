# homeworck 8.1
from itertools import count

def add_one(some_list):
    # с помошью метода map преобразуем список в строку после int делает из строки целое число + 1
    strListPlusOne = (int(''.join(map(str,some_list))))+1
    # strListPlusOne преобразую в строку чтобы перебрать каждый элемент масива и записать в новый список
    newListOfNumbers = [int(a) for a in str(strListPlusOne)]
    return newListOfNumbers

# homeworck 8.2
import string

def is_palindrome (text):
    text = text.upper().replace(" ", "") # удаление пробелов и изменнеиние регистра символов
    for symbol in string.punctuation: #  цикл для удаления из строки всего что содержится в string.punctuation
        text = text.replace(symbol, "")
    if text == text[::-1]: # сравнения строки в обратном порядке с обычной главной строкой
        return True
    else:
        return False

# homeworck 8.3
def find_unique_value(some_list):
    for element in range(len(some_list)): # циклом прохожу по всему списку
        if some_list.count(some_list[element]) == 1:  # проверяю каждую цифру на уникальность с помощь метода count
            return some_list[element] # возвращаю уникальное число


print("homeworck 8.1")
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
print("homeworck 8.2")

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

print("homeworck 8.3")

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")



