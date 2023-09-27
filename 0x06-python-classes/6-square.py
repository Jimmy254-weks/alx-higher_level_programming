class Square:
    """This class represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Create a square with a given size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, ensuring it's a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be a non-negative integer")
        self.__size = value

    @property
    def position(self):
        """Get or set the position of the square as a tuple of two positive integers."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square as a tuple of two positive integers."""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("Position must be a tuple of two positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using '#' characters and spaces, respecting the position."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]

        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")
