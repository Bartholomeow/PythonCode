import figures
import math
import pytest

class TestCircle:
    def test_init_without_parameters(self):
        a = figures.Circle()
        assert a.get_area() == math.pi
        assert a.get_perimeter() == 2 * math.pi

    def test_radius_equal_1(self):
        a = figures.Circle(1)
        assert a.get_area() == math.pi
        assert a.get_perimeter() == 2 * math.pi

    def test_radius_equal_2(self):
        a = figures.Circle(2)
        assert a.get_area() == 4 * math.pi
        assert a.get_perimeter() == 4 * math.pi

    def test_radius_equal_0(self):
        a = figures.Circle(0)
        assert a.get_area() == 0
        assert a.get_perimeter() == 0

    def test_radius_is_float(self):
        a = figures.Circle(2.5)
        assert a.get_area() == 2.5 ** 2 * math.pi
        assert a.get_perimeter() == 5 * math.pi

    def test_negative_radius(self):
        with pytest.raises(Exception) as excinfo:   
            a = figures.Circle(-1)   
        assert str(excinfo.value) == "Radius can not be less than zero"

class TestSquare:
    def test_init_without_parameters(self):
        a = figures.Square()
        assert a.get_area() == 1
        assert a.get_perimeter() == 4

    def test_side_equal_1(self):
        a = figures.Square(1)
        assert a.get_area() == 1
        assert a.get_perimeter() == 4

    def test_side_equal_2(self):
        a = figures.Square(2)
        assert a.get_area() == 4
        assert a.get_perimeter() == 8

    def test_side_equal_0(self):
        a = figures.Square(0)
        assert a.get_area() == 0
        assert a.get_perimeter() == 0

    def test_side_is_float(self):
        a = figures.Square(2.5)
        assert a.get_area() == 2.5 ** 2
        assert a.get_perimeter() == 10

    def test_negative_side(self):
        with pytest.raises(Exception) as excinfo:   
            a = figures.Square(-1)   
        assert str(excinfo.value) == "Side can not be less than zero"


class TestRectangle:
    def test_init_without_parameters(self):
        a = figures.Rectangle()
        assert a.get_area() == 1
        assert a.get_perimeter() == 4

    def test_side_equal_1(self):
        a = figures.Rectangle(1)
        assert a.get_area() == 1
        assert a.get_perimeter() == 4

    def test_sides_equal_2_2(self):
        a = figures.Rectangle(2, 2)
        assert a.get_area() == 4
        assert a.get_perimeter() == 8

    def test_sides_equal_1_3(self):
        a = figures.Rectangle(1, 3)
        assert a.get_area() == 3
        assert a.get_perimeter() == 8

    def test_sides_equal_0(self):
        a = figures.Rectangle(0, 0)
        assert a.get_area() == 0
        assert a.get_perimeter() == 0

    def test_one_side_equal_0(self):
        a = figures.Rectangle(2, 0)
        assert a.get_area() == 0
        assert a.get_perimeter() == 0

    def test_side_is_float(self):
        a = figures.Rectangle(2.5, 5)
        assert a.get_area() == 12.5
        assert a.get_perimeter() == 15

    def test_negative_sideA(self):
        with pytest.raises(Exception) as excinfo:   
            a = figures.Rectangle(-1, 2)   
        assert str(excinfo.value) == "Side can not be less than zero"

    def test_negative_sideB(self):
        with pytest.raises(Exception) as excinfo:   
            a = figures.Rectangle(1, -2)   
        assert str(excinfo.value) == "Side can not be less than zero"

    def test_negative_sides(self):
        with pytest.raises(Exception) as excinfo:   
            a = figures.Rectangle(-1, -2)   
        assert str(excinfo.value) == "Side can not be less than zero"

    def test_negative_side_and_zero_side(self):
        with pytest.raises(Exception) as excinfo:   
            a = figures.Rectangle(-1, 0)   
        assert str(excinfo.value) == "Side can not be less than zero"


class TestCuboid:
    def test_init_without_parameters(self):
        a = figures.Cuboid()
        assert a.get_area() == 6
        assert a.get_perimeter() == 12
        assert a.get_volume() == 1

    def test_side_equal_1(self):
        a = figures.Cuboid(1)
        assert a.get_area() == 6
        assert a.get_perimeter() == 12
        assert a.get_volume() == 1

    def test_sides_equal_2_2(self):
        a = figures.Cuboid(2, 2, 2)
        assert a.get_area() == 24
        assert a.get_perimeter() == 24
        assert a.get_volume() == 8

    def test_sides_equal_1_3(self):
        a = figures.Cuboid(1, 2, 3)
        assert a.get_area() == 22
        assert a.get_perimeter() == 24
        assert a.get_volume() == 6

    def test_sides_equal_0(self):
        a = figures.Cuboid(0, 0, 0)
        assert a.get_area() == 0
        assert a.get_perimeter() == 0
        assert a.get_volume() == 0

    def test_one_side_equal_0(self):
        a = figures.Cuboid(1, 2, 0)
        assert a.get_area() == 0
        assert a.get_perimeter() == 0
        assert a.get_volume() == 0

    def test_two_sides_equal_0(self):
        a = figures.Cuboid(1, 0, 0)
        assert a.get_area() == 0
        assert a.get_perimeter() == 0
        assert a.get_volume() == 0

    def test_side_is_float(self):
        a = figures.Cuboid(0.25, 1, 4)
        assert a.get_area() == 10.5
        assert a.get_perimeter() == 21
        assert a.get_volume() == 1

    def test_negative_sideA(self):
        with pytest.raises(Exception) as excinfo:   
            a = figures.Cuboid(-1, 2, 3)   
        assert str(excinfo.value) == "Side can not be less than zero"

    def test_negative_sideB(self):
        with pytest.raises(Exception) as excinfo:   
            a = figures.Cuboid(1, -2, 3)   
        assert str(excinfo.value) == "Side can not be less than zero"

    def test_negative_sideC(self):
        with pytest.raises(Exception) as excinfo:   
            a = figures.Cuboid(1, 2, -3)   
        assert str(excinfo.value) == "Side can not be less than zero"
    
    def test_two_negative_sides(self):
        with pytest.raises(Exception) as excinfo:   
            a = figures.Cuboid(1, -2, -3)   
        assert str(excinfo.value) == "Side can not be less than zero"

    def test_negative_sides(self):
        with pytest.raises(Exception) as excinfo:   
            a = figures.Cuboid(-1, -2, -3)   
        assert str(excinfo.value) == "Side can not be less than zero"

    def test_negative_side_and_zero_side(self):
        with pytest.raises(Exception) as excinfo:   
            a = figures.Cuboid(-1, 0, 1)   
        assert str(excinfo.value) == "Side can not be less than zero"

    
class TestCube:
    def test_init_without_parameters(self):
        a = figures.Cube()
        assert a.get_area() == 6
        assert a.get_perimeter() == 12
        assert a.get_volume() == 1

    def test_side_equal_1(self):
        a = figures.Cube(1)
        assert a.get_area() == 6
        assert a.get_perimeter() == 12
        assert a.get_volume() == 1

    def test_side_equal_2(self):
        a = figures.Cube(2)
        assert a.get_area() == 24
        assert a.get_perimeter() == 24
        assert a.get_volume() == 8

    def test_side_equal_0(self):
        a = figures.Cube(0)
        assert a.get_area() == 0
        assert a.get_perimeter() == 0
        assert a.get_volume() == 0

    def test_side_is_float(self):
        a = figures.Cube(1.5)
        assert a.get_area() == 13.5
        assert a.get_perimeter() == 18
        assert a.get_volume() == 1.5 ** 3

    def test_negative_side(self):
        with pytest.raises(Exception) as excinfo:   
            a = figures.Cube(-1)   
        assert str(excinfo.value) == "Side can not be less than zero"


class TestSphere:
    def test_init_without_parameters(self):
        a = figures.Sphere()
        assert a.get_area() == 4 * math.pi
        assert a.get_perimeter() == math.inf
        assert a.get_volume() == 4 / 3 * math.pi

    def test_radius_equal_1(self):
        a = figures.Sphere(1)
        assert a.get_area() == 4 * math.pi
        assert a.get_perimeter() == math.inf
        assert a.get_volume() == 4 / 3 * math.pi

    def test_radius_equal_2(self):
        a = figures.Sphere(2)
        assert a.get_area() == 16 * math.pi
        assert a.get_perimeter() == math.inf
        assert a.get_volume() == 32 / 3 * math.pi

    def test_radius_equal_0(self):
        a = figures.Sphere(0)
        assert a.get_area() == 0
        assert a.get_perimeter() == 0
        assert a.get_volume() == 0

    def test_radius_is_float(self):
        a = figures.Sphere(1.5)
        assert a.get_area() == 4 * math.pi * 1.5 ** 2
        assert a.get_perimeter() == math.inf
        assert a.get_volume() == 4 / 3 * math.pi * 1.5 ** 3

    def test_negative_radius(self):
        with pytest.raises(Exception) as excinfo:   
            a = figures.Sphere(-1)   
        assert str(excinfo.value) == "Radius can not be less than zero"