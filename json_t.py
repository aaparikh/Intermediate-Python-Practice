from inspect import ClassFoundException
import json

#read json file to dictionary
person = json.load(open('./sample.json'))
print(type(person))

#convert dict to json str with pretty formatting (provided by indentation)
#sort_keys prints the keys in alphabetical order
wperson = json.dumps(person,indent=4,sort_keys=True)
print(type(wperson))

#write dict to files
with open('test.json','w') as f:
    json.dump(person,f,indent=4)



#ecoding a custom object
class User:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

def encode_o(o):
    if isinstance(o,User):
        return {'name':o.name, 'age':o.age, o.__class__.__name__:True}
    else:
        raise TypeError('Object of the type user is not JSON serializable')

user = User('Atharva',20)
with open('test.json','w') as f:
    json.dump(user,f,indent=4)

def decode_o(dct):
    if User.__name__ in dct:
        return dict(name=dct['name'],age=dct['age'])
    return dct

#important here is the ability to encode and decode custom objects using json