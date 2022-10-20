class Rectangle:
    """직사각형 클래스"""

    def __init__(self, width, height):
        """세로와 가로"""
        self.width = width
        self.height = height

    def area(self):
        """넓이 계산 메소드"""
        return self.width * self.height

    @property
    def width(self):
        """가로 변수 getter 메소드"""
        return self._width

    @width.setter
    def width(self, value):
        """가로 변수 setter 메소드"""
        self._width = value if value > 0 else 1

    @property
    def height(self):
        """세로 변수 getter 메소드"""
        return self._height

    @height.setter
    def height(self, value):
        """세로 변수 setter 메소드"""
        self._height = value if value > 0 else 1


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    @property
    def width(self):
        """가로 변수 getter 메소드"""
        return self._width

    @width.setter
    def width(self, value):
        """가로 변수 setter 메소드"""
        self._width = value if value > 0 else 1
        self._height = value if value > 0 else 1

    @property
    def height(self):
        """세로 변수 getter 메소드"""
        return self._height

    @height.setter
    def height(self, value):
        """세로 변수 setter 메소드"""
        self._width = value if value > 0 else 1
        self._height = value if value > 0 else 1


rectangle_1 = Rectangle(4, 6)
rectangle_2 = Square(2)

rectangle_1.width = 3
rectangle_1.height = 7

print(rectangle_1.area())

rectangle_2.width = 3
rectangle_2.height = 7
# heignt와 width가 같기 때문에 둘다 7로 설정되어서 49가 출력됨. 오버라이딩 안하고 그대로 가지고 와 가로와 세로를 다르게 설정할 수도 있기 때문에 정사각형의/
# 정의에서 벗어남.

print(rectangle_2.area())
