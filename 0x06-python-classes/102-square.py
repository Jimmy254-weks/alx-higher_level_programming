class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """Initialize a new square with a given size."""
        self.size = size

    @property
    def size(self):
        """Get or set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, ensuring it's a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be a non-negative integer")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Define the equality comparison between two Square objects based on their areas."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the inequality comparison between two Square objects based on their areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the less than comparison between two Square objects based on their areas."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the less than or equal comparison between two Square objects based on their areas."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the greater than comparison between two Square objects based on their areas."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the greater than or equal comparison between two Square objects based on their areas."""
        return self.area() >= other.area()

