def create_array(x, y, z, w):
     return [[[w for _ in range(z)] for _ in range(y) for _ in range(x)]]
array = create_array(3, 4, 5, 11)
print(array)
