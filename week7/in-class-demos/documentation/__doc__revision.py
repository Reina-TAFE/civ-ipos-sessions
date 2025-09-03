# Revision: docstrings versus multiline strings
# TODO show doc variable
# I am a comment
# "I might be a docstring"
"""I am more likely to be a docstring, but still just a multiline string"""


def print_docs():
    print(f"{__doc__}")


class Cat:
    """Docstring for cat... best animal in the world"""

    def meow(self, length):
        """Docstring for a method or function"""
        pass

    """Remember: a multiline string anywhere else is just a string
    I am just a string, for example."""


print(help(Cat.meow))

cat = Cat()
print(print_docs())
