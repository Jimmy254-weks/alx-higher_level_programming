class Square:
    """This class represents a square."""

    def __init__(self, size):
        """Create a square with a given size."""
        self.__size = size

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
