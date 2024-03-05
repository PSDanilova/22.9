def binary_search(array, element, left, right):
    if left > right:
            return False
    middle = (right + left) // 2
    if element == array[middle]:
        if array[middle - 1] < element and element <= array[middle]:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
    elif element == array[middle - 1]:
            return binary_search(array, element, left, middle - 1)
    else:
            return binary_search(array, element, middle + 1, right)
array = list(map(float, input("Введите число в любом порядке, через пробел: ").split()))
element = float(input("Введите любое число из введеного списка: "))
array = sorted(array)
print(array)
left = float(array[0])
right = float(array[-1])
if element < left or element > right:
    print('Числа нет в диапазоне')
else:
    print(binary_search(array, element, 0, len(array) - 1))