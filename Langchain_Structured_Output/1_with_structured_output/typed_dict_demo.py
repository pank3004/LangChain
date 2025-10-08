# normal dictionary
d={'name': 'Pankaj', 'age': 22}
print(d)

# typed dictionary: 
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {'name': 'Pankaj', 'age': 22}
new_person_2: Person = {'name': 'Pankaj', 'age': '22'}  # this will not validate

print(new_person)
print(new_person_2)


# | Feature              | Normal Dictionary (`dict`)                             | Typed Dictionary (`TypedDict`)                                                                                                             |
# | -------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
# | **Definition**       | A normal `dict` is a collection of key-value pairs.    | A `TypedDict` (from `typing` module) is a special dictionary that defines the expected types of keys and values.                           |
# | **Type Checking**    | Keys and values can be of any type — no type checking. | It enforces **type hints** — each key must have a specific type (checked by tools like `mypy`).                                            |
# | **Use Case**         | When you want flexibility — any key/value.             | When you want **structure** — like defining a schema for your dict.                                                                        |
# | **Example**          | `person = {"name": "Pankaj", "age": 22}`               | `python from typing import TypedDict  class Person(TypedDict):     name: str     age: int  person: Person = {"name": "Pankaj", "age": 22}` |
# | **Runtime Behavior** | Python doesn’t check types at runtime.                 | Still no runtime check, but static analyzers (like mypy) can catch errors early.                                                           |
# | **Error Checking**   | You can add any key or wrong type without error.       | Type checkers will **warn** if you miss a key or put a wrong type.                                                                         |
