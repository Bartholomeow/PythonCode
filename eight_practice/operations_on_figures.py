import figures


circle = figures.Circle(3)
square = figures.Square(2)
rectangle = figures.Rectangle(2, 4)

for third_dimension_figure in [circle, square, rectangle]:
    print(
        f'Area of {type(third_dimension_figure).__name__} = {third_dimension_figure.get_area()}')
    print(
        f'Perimeter of {type(third_dimension_figure).__name__} = {third_dimension_figure.get_perimeter()}')
    print()

sphere = figures.Sphere(3)
cube = figures.Cube(3)
cuboid = figures.Cuboid(2, 4, 5)

for third_dimension_figure in [sphere, cube, cuboid]:
    print(
        f'Area of {type(third_dimension_figure).__name__} = {third_dimension_figure.get_area()}')
    print(
        f'Perimeter of {type(third_dimension_figure).__name__} = {third_dimension_figure.get_perimeter()}')
    print(
        f'Volume of {type(third_dimension_figure).__name__} = {third_dimension_figure.get_volume()}')
    print()