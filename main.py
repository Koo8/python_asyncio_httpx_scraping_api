"""
How to make custom class Json serializable - 4 methods
How to make json.loads() to return a custom class objeact instead of string type - using object hooks
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
        """ if json.loads() return dict is ok, use this simple return"""
        # return o.__dict__
        """ if json.loads() return the object(person), use this return with a added key of the class name for conditional checking """
        return {"name":o.name, 'email':o.email, 'children': o.children, o.__class__.__name__: True}


# print(PersonEnCoder().encode(mom)) # to test our if encoder works
momJson = json.dumps(mom, indent=4, cls=PersonEnCoder)
print(momJson)

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
# print(mom2_json)
# print(json.loads(mom2_json)) 

""" custom deCoder for 'object_hook' param for json.loads() to return an object(person) """

def person_decoder(dic_tionary):
    if Person.__name__ in dic_tionary:
        return Person(name=dic_tionary['name'], email=dic_tionary['email'], children=dic_tionary['children'])
    else:
        return dic_tionary
    
# p = json.loads(momJson, object_hook=person_decoder)
# print(p.children[0].name)
  
def person_decoder_without_class_name(dic):
    return Person(name=dic['name'], email=dic['email'], children=dic['children'])

p1 = json.loads(momJson, object_hook=person_decoder_without_class_name)
print(p1.name)

