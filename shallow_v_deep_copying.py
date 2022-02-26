"""
- shallow copy : one level deep, only references of nested child objects
- deep copy : full independent copy
"""
#for immutable types this is not an issue but for mutable types we have to be careful
import copy

org = [0,1,2,3,4]

#shallow copy
cpy = copy.copy(org)
#2 other ways to do this :
    # cpy = org.copy()
    # cpy = list(org)
    # cpy = org[:]
cpy[0] = -1
print(org)
print(cpy)
#here original won't get affected

#But this shallow copy works for only one level
org2 = [[1,2],[3,4]] #2d array
cpy = org2.copy()
cpy[0][1] = 6
print(org2)
print(cpy)
#changes are made in both the lists

#to solve this we use deepcopy, this makes a true copy of a list
org2 = [[1,2],[3,4]]
cpy = copy.deepcopy(org2)
cpy[0][1] = -1
print(org2)
print(cpy)


class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

class Company:
    def __init__(self,boss,employee) -> None:
        self.boss = boss
        self.employee = employee
    
p1 = Person('Atharva',20)
p2 = Person('Aryan',21)
c = Company(p1,p2)
#shallow copy
c_clone = copy.copy(c)
c_clone.boss.age = 60 #changing age will change the values in both the objects as its a shallow copy (one level)
print(c.boss.age)
print(c_clone.boss.age)

#deep copy
c_clone_deep = copy.deepcopy(c)
c_clone_deep.boss.age = 62 #here the original object will remain unaffected
print(c.boss.age)
print(c_clone_deep.boss.age)