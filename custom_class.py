class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # __iter__ method to make the class iterable
    def __iter__(self):
        # We yield the length first, followed by the width
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage:
rect = Rectangle(10, 20)

# Iterating over the instance
for dimension in rect:
    print(dimension)
