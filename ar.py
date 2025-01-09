import array as arr
a = arr.array("I", [113,243,233])
print("The new array is :",end =" ")
for I in range(0, 3):
    print(a[I], end = " ")
print()
b = arr.array("d", [2.5, 3.6, 1.5])
print("the new array is : ", end=" ")
for I in range(0, 3):
    print(b[I], end = " ")
print()
a.insert(1, 4)
print("array after insert :", end = " ")
for I in a:
    print(I, end= " ")
print()
b.append(4.2)
print("array after append :", end = " ")
for I in b:
    print(I, end = " ")
print()