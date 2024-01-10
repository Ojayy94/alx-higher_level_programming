#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """My class function"""

    def print_sorted(self):
        """Print a list in sorted ascending order"""

        print(sorted(self))
