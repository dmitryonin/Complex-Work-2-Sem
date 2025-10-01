class Quadrilateral:
    def __init__(self, a, b, c, d):
        self.check_sides(a, b, c, d)
        self.check_exist(a, b, c, d)

        self.A = a
        self.B = b
        self.C = c
        self.D = d

    def check_sides(self, *sides):
        for side in sides:
            if not isinstance(side, (int, float)):
                raise TypeError("Все стороны должны быть числами.")
            if side <= 0:
                raise ValueError("Все стороны должны быть положительными.")

    def check_exist(self, a, b, c, d):
        if not (a < b + c + d and b < a + c + d and c < a + b + d and d < a + b + c):
            raise ValueError("Четырехугольник с такими сторонами не существует")

    def perimeter(self):
        return self.A + self.B + self.C + self.D

    def display_info(self):
        print(f"Четырехугольник со сторонами: {self.A}, {self.B}, {self.C}, {self.D}")
        print(f"Периметр: {self.perimeter()}")


class Rectangle(Quadrilateral):
    def __init__(self, length, width):
        super().__init__(length, width, length, width)

    def display_info(self):
        print(f"Прямоугольник со сторонами: {self.A} (длина), {self.B} (ширина)")
        print(f"Периметр: {self.perimeter()}")


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def display_info(self):
        print(f"Квадрат со стороной: {self.A}")
        print(f"Периметр: {self.perimeter()}")


def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Ошибка: значение должно быть положительным!")
                continue
            return value
        except ValueError:
            print("Ошибка: введите число!")


print("Программа для работы с четырехугольниками")
print("=" * 40)

while True:
    print("\nВыберите тип фигуры:")
    print("1 - Четырехугольник")
    print("2 - Прямоугольник")
    print("3 - Квадрат")
    print("0 - Выход")

    choice = input("Ваш выбор: ")

    if choice == "0":
        print("Выход из программы...")
        break

    elif choice == "1":
        print("\nСоздание четырехугольника:")
        a = get_positive_number("Введите сторону A: ")
        b = get_positive_number("Введите сторону B: ")
        c = get_positive_number("Введите сторону C: ")
        d = get_positive_number("Введите сторону D: ")

        try:
            quadrilateral = Quadrilateral(a, b, c, d)
            print("\nЧетырехугольник успешно создан!")
            quadrilateral.display_info()
        except (TypeError, ValueError) as e:
            print(f"Ошибка: {e}")

    elif choice == "2":
        print("\nСоздание прямоугольника:")
        length = get_positive_number("Введите длину: ")
        width = get_positive_number("Введите ширину: ")

        try:
            rectangle = Rectangle(length, width)
            print("\nПрямоугольник успешно создан!")
            rectangle.display_info()
        except (TypeError, ValueError) as e:
            print(f"Ошибка: {e}")

    elif choice == "3":
        print("\nСоздание квадрата:")
        side = get_positive_number("Введите сторону квадрата: ")

        try:
            square = Square(side)
            print("\nКвадрат успешно создан!")
            square.display_info()
        except (TypeError, ValueError) as e:
            print(f"Ошибка: {e}")

    else:
        print("Неверный выбор! Попробуйте снова.")