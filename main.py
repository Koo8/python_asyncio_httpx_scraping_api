"""
How to make custom class Json serializable - 4 methods
"""
import json
from json import JSONEncoder
from typing import Any

class Person():
    def __init__(self, name, email, children=None):
        self.name = name
        self.email = email
        self.children = children

grandson = Person('Tom', 't@email.com')
son = Person("John", 'j@email.com')
daughter = Person("Lucy", 'l@email.com', grandson)
mom = Person("nancy",'n@email.com', [son, daughter] )

""" Method 1: use subclass JSONEncoder to override default() method """
class PersonEnCoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        return o.__dict__


# print(PersonEnCoder().encode(mom)) # to test our if encoder works
momJson = json.dumps(mom, indent=4, cls=PersonEnCoder)
# print(momJson)

mom = json.loads(momJson)
# print(mom)

""" Method 2: add toJson() to the class """

class Person_1():
    def __init__(self, name, email, children=None):
        self.name = name
        self.email = email
        self.children = children
    
    def toJson(self):
        return json.dumps(self, default=lambda o : o.__dict__, indent=4)
    


grandson = Person_1('Tom', 't@email.com')
son = Person_1("John", 'j@email.com')
daughter = Person_1("Lucy", 'l@email.com', grandson)
mom1 = Person_1("nancy",'n@email.com', [son, daughter] )


# print(mom.toJson())
# print(json.loads(mom.toJson()))

""" Method 3: use jsonpickle package """
    
import jsonpickle

person_pickled = jsonpickle.encode(mom,  indent=4)

# print(person_pickled)
# print(json.loads(person_pickled))


""" Method 4: inheriting from dict class """

class Person_2(dict):
    def __init__(self, name, email, children=None):
        dict.__init__(self, name=name, email=email,children=children)

grandson = Person_2('Tom', 't@email.com')
son = Person_2("John", 'j@email.com')
daughter = Person_2("Lucy", 'l@email.com', grandson)
mom2 = Person_2("nancy",'n@email.com', [son, daughter] )

mom2_json = json.dumps(mom2, indent=4)
print(mom2_json)
print(json.loads(mom2_json))