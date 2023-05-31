def removeExtreme(number_array, num):
    sorted_array = sorted(number_array)
    sorted_array = sorted_array[num:-num]
    return sorted_array
n = int(input("Enter the number of elements in array:"))
array = []
print("Enter the elements:")
for i in range(0, n):
    element = int(input())
    array.append(element)
print("Array is:", array)
number = int(input("Enter the no of largest and smallest nos to be removed:"))
print(removeExtreme(array, number))
