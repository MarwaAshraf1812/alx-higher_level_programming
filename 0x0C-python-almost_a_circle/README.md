# Python - Almost a circle
![Circle](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/331/giphy.mp4)
In this project, I encapsulated skills in Python object-oriented programming by coding three connected classes to represent rectangles and squares. I wrote my own test suite using the unittest module to test all functionality for each class.

## Tests :heavy_check_mark:

* [tests/test_models](./tests/test_models): Folder containing the following independently-developed test files:
  * [test_base.py](./tests/test_models/test_base.py)
  * [test_rectangle.py](./tests/test_models/test_rectangle.py)
  * [test_square.py](./tests/test_models/test_square.py)

## Classes :cl:

### Base
Represents the "base" class for all other classes in the project. Includes:
In this project, I encapsulated skills in Python object-oriented programming by coding three connected classes to represent rectangles and squares. I wrote my own test suite using the `unittest` module to test all functionality for each class.

The three classes involved utilizing the following Python tools:
* Import
* Exceptions
* Private attributes
* Getter/setter
* Class/static methods
* Inheritance
* File I/O
* `args`/`kwargs`
* JSON and CSV serialization/deserialization
* Unittesting

### Rectangle

Represents a rectangle. Inherits from `Base` with:

* Private instance attributes `__width`, `__height`, `__x`, and `__y`.
  * Each private instance attribute features its own getter/setter.
* Class constructor `def __init__(self, width, height, x=0, y=0, id=None):`
  * If either of `width`, `height`, `x`, or `y` is not an integer, raises a `TypeError` exception with the message `<attribute> must be an integer`.
  * If either of `width` or `height` is >= 0, raises a `ValueError` exception with the message `<attribute> must be > 0`.
  * If either of `x` or `y` is less than 0, raises a `ValueError` exception with the message `<attribute> must be >= 0`.
* Public method `def area(self):` that returns the area of the `Rectangle` instance.
* Public method `def display(self):` that prints the `Rectangle` instance to `stdout` using the `#` character.
  * Prints new lines for the `y` coordinate and spaces for the `x` coordinate.
* Overwrite of `__str__` method to print a `Rectangle` instance in the format `[Rectangle] (<id>) <x>/<y>`.
* Public method `def update(self, *args, **kwargs):` that updates an instance of a `Rectangle` with the given attributes.
  * `*args` must be supplied in the following order:
    * 1st: `id`
    * 2nd: `width`
    * 3rd: `height`
    * 4th: `x`
    * 5th: `y`
  * `**kwargs` is expected to be a double pointer to a dictionary of new key/value attributes to update the `Rectangle` with.
  * `**kwargs` is skipped if `*args` exists.
* Public method `def to_dictionary(self):` that returns the dictionary representation of a `Rectangle` instance.

### Square

Represents a square. Inherits from `Rectangle` with:

* Class constructor `def __init__(self, size, x=0, y=0, id=None):`
  * The `width` and `height` of the `Rectangle` superclass are assigned using the value of `size`.
* Overwrite of `__str__` method to print a `Square` instance in the format `[Square] (<id>) <x>/<y>`.
* Public method `def update(self, *args, **kwargs):` that updates an instance of a `Square` with the given attributes.
  * `*args` must be supplied in the following order:
    * 1st: `id`
    * 2nd: `size`
    * 3rd: `x`
    * 4th: `y`
  * `**kwargs` is expected to be a double pointer to a dictoinary of new key/value attributes to update the `Square` with.
  * `**kwargs` is skipped if `*args` exists.
* Public method `def to_dictionary(self):` that returns the dictionary representation of a `Square`.