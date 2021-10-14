from unittest.mock import Mock

mock = Mock(
    return_value = 25
)
print(mock)
# The return_value attribute is used to configure the return value of a mock Method when it is invoked

# The return_value attribute also shares the same mock object ID as when you invoke the mock object as a method
# print(mock.return_value)
# mock.return_value = 25
print(mock())

stuntman = Mock()
stuntman.jump_off_building.return_value = "Oh no, my leg"
stuntman.light_on_fire.return_value = "It burns!"

print(stuntman.light_on_fire())
print(stuntman.jump_off_building())