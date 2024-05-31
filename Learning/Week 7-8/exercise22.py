integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]
binary_dict = {a: b for a, b in zip(integer, binary)}
print(binary_dict)

integer = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = [x*(-1) for x in integer]
print(additive_inverse)

integer2 = [1, -1, 2, -2, 3, -3]
sq_set = {x**2 for x in integer2}
print(sq_set)