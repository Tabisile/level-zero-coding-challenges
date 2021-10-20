def area(x,y,z):
    s = 1/2(x + y +z)
    area_of_a_triangle = (s * (s - x) * (s - y) * (s - z)) ** 1/2
    return area_of_a_triangle
