# MagicMock is a subclass of mock

from unittest.mock import Mock, MagicMock

# The major difference between Mock and MagicMock is that the latter support magic (dunder) methods

plain_mock = Mock()
magic_mock = MagicMock()

# print(len(plain_mock()))
print(len(magic_mock()))

# The MagicMock object supports indexing while the plain Mock object does not
# __getitem__ is the dunder method the MagiMock object uss for this purpose

# print(plain_mock[3])
print(magic_mock[3])
# It's always going to return the same default MagicMock object no matter the index position targeted

# The return value for the MagicMock object can be changed if we know the actual dunder method working behind the scenes
# Length is determined by the __len__ method
magic_mock.__len__.return_value = 50
print(len(magic_mock))

# Truthiness is determined by __bool__ method
magic_mock.__bool__.return_value = False;
if magic_mock:
    print('Hello!')

# For indexing, we call __getitem__
magic_mock.__getitem__.return_value = 100
print(magic_mock[3])

