class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """Create a square with a given size, ensuring it's a non-negative integer."""
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be a non-negative integer")
        self.__size = size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size
