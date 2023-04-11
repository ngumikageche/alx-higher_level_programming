#!/usr/bin/python3
""" Define a class list: """


class MyList(list):
    """Impliments sorted printing for the built-in list class."""

    def print_sorted(self):
        """print a list in sorted sceding order."""
        print(sorted(self))
