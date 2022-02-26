#collections library
# https://www.geeksforgeeks.org/python-collections-module/

#========================= Counter =========================
from collections import Counter, OrderedDict

#Counter stores the dictionary items as keys and their count as values
a = "abcccbaaeee"
my_counter = Counter(a)
print(my_counter)
#get the most commom (k) elements
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements())) #returns all the elements so we can iterate on them

#========================= namedtuple =========================
from collections import namedtuple
#nametuple is an easy to create lightweight object type similar to struct
Point = namedtuple('Point','x,y')
p1 = Point(4,3)
print(f'x value - {p1.x}, y value - {p1.y}')

#========================= OrderedDict =========================
#Like a regular dictionary but can remember the order in which answers were inserted
#this has become less important now since the built-in dictionary class also has the ability
# to remember the order since python3.6 
od = OrderedDict()
od['a'] = 1
od['c'] = 3
od['b'] = 2
print(od)

#========================= defaultdict =========================
from collections import defaultdict
#same as regular dict, difference being that default value for a key has not been set yet
#this ensures that key errors don't occur as when a invalid key is called then the value
# of default datatype is provided
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['z']) #does not exist so default val of int (0) is returned

#========================= deque =========================
from collections import deque
#doubly ended queue
#insertion and deletion is O(1)
#for list it is O(n)
d = deque()
d.append(1)
d.appendleft(2)
print(d) # deque([2, 1])
d.pop()
print(d) # deque([2])
d.appendleft(1)
print(d) # deque([1, 2])
d.popleft()
print(d) # deque([2])
d.extend([5,4,6])
d.extendleft([8,9]) #revrese of the provided list gets appended at the start
print(d) # deque([9, 8, 2, 5, 4, 6])