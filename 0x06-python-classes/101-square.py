class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.set_size(size)
        self.set_position(position)

    @property
    def get_size(self):
        return self.__size

    @get_size.setter
    def set_size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be non-negative")
        self.__size = value

    @property
    def get_position(self):
        return self.__position

    @get_position.setter
    def set_position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("Position must be a tuple of 2 positive integers")
        self.__position = value

    def calculate_area(self):
        return self.__size * self.__size

    def display_square(self):
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]

        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
