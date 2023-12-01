# The ``3-say_my_name`` module
============================================
How to use 3-say_my_name.py
============================================

This library has one function called ``say_my_name()``

``say_my_name()`` prints a person's first name and last name.

Importing the function say_my_name.
    >>> say_my_name = __import__('3-say_my_name').say_my_name

Passing first_name and last_name correctly.
    >>> say_my_name("yordanos", "tarekegn")
    My name is Wendy Munyasi

    >> say_my_name("bezawit")
    My name is bezawit

Passing last_name as None.
    >>> say_my_name("yordanos", None)
    Traceback (most recent call last):
        ...
    TypeError: last_name must be a string

Passing first_name and last_name as None.
    >>> say_my_name(None, None)
    Traceback (most recent call last):
        ...
    TypeError: first_name must be a string

Passing first name as None.
    >>> say_my_name(None, "bezawit")
    Traceback (most recent call last):
        ...
    TypeError: first_name must be a string

Passing wrong types as first_name and last_name
    >>> say_my_name(1, "Bezawit")
    Traceback (most recent call last):
        ...
    TypeError: first_name must be a string

    >>> say_my_name("ayra", [4])
    Traceback (most recent call last):
        ...
    TypeError: last_name must be a string

Passing more than two arguments to say_my_name().
    >>> say_my_name("ayra", "Bezawit", "wereta") #doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    TypeError: say_my_name() takes from 1 to 2 positional arguments but ...
