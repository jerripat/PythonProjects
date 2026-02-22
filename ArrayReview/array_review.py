from array import array

int_array = array('i', [1, 2, 3, 4, 5])
print("Original Array:", len(int_array))

int_array.append(6)
print("After Appending:", len(int_array))