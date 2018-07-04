
def add_numbers(x, y):
    return x + y

add_numbers(1, 2)

def add_numbers(x,y,z=None):
    if (z==None):
        return x+y
    else:
        return x+y+z

print(add_numbers(1, 2))
print(add_numbers(1, 2, 3))

def add_numbers(x, y, z=None, flag=False):
    if (flag):
        print('Flag is true!')
    if (z==None):
        return x + y
    else:
        return x + y + z
    
print(add_numbers(1, 2, flag=True))

def add_numbers(x,y):
    return x+y

a = add_numbers
a(1,2)

type('This is a string')

type(None)

type(1)

type(1.0)

type(add_numbers)

x = (1, 'a', 2, 'b')
type(x)

x = [1, 'a', 2, 'b']
type(x)

x.append(3.3)
print(x)

for item in x:
    print(item)

i=0
while( i != len(x) ):
    print(x[i])
    i = i + 1

[1,2] + [3,4]

[1]*3

1 in [1, 2, 3]

x = 'This is a string'
print(x[0]) #first character
print(x[0:1]) #first character, but we have explicitly set the end character
print(x[0:2]) #first two characters


x[-1]

x[-4:-2]

x[:3]

x[3:]

firstname = 'Christopher'
lastname = 'Brooks'

print(firstname + ' ' + lastname)
print(firstname*3)
print('Chris' in firstname)


firstname = 'Christopher Arthur Hansen Brooks'.split(' ')[0] # [0] selects the first element of the list
lastname = 'Christopher Arthur Hansen Brooks'.split(' ')[-1] # [-1] selects the last element of the list
print(firstname)
print(lastname)

'Chris' + 2

'Chris' + str(2)

x = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com'}
x['Christopher Brooks'] # Retrieve a value by using the indexing operator


x['Kevyn Collins-Thompson'] = None
x['Kevyn Collins-Thompson']

for name in x:
    print(x[name])

for email in x.values():
    print(email)

for name, email in x.items():
    print(name)
    print(email)

x = ('Christopher', 'Brooks', 'brooksch@umich.edu')
fname, lname, email = x

fname

lname

x = ('Christopher', 'Brooks', 'brooksch@umich.edu', 'Ann Arbor')
fname, lname, email = x

print('Chris' + 2)

print('Chris' + str(2))

sales_record = {
'price': 3.24,
'num_items': 4,
'person': 'Chris'}

sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'

print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items']*sales_record['price']))


import csv

%precision 2

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))
    
mpg[:3] # The first three dictionaries in our list.

len(mpg)

mpg[0].keys()

sum(float(d['cty']) for d in mpg) / len(mpg)

sum(float(d['hwy']) for d in mpg) / len(mpg)

cylinders = set(d['cyl'] for d in mpg)
cylinders

CtyMpgByCyl = []

for c in cylinders: # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for d in mpg: # iterate over all dictionaries
        if d['cyl'] == c: # if the cylinder level type matches,
            summpg += float(d['cty']) # add the cty mpg
            cyltypecount += 1 # increment the count
    CtyMpgByCyl.append((c, summpg / cyltypecount)) # append the tuple ('cylinder', 'avg mpg')

CtyMpgByCyl.sort(key=lambda x: x[0])
CtyMpgByCyl

vehicleclass = set(d['class'] for d in mpg) # what are the class types
vehicleclass

HwyMpgByClass = []

for t in vehicleclass: # iterate over all the vehicle classes
    summpg = 0
    vclasscount = 0
    for d in mpg: # iterate over all dictionaries
        if d['class'] == t: # if the cylinder amount type matches,
            summpg += float(d['hwy']) # add the hwy mpg
            vclasscount += 1 # increment the count
    HwyMpgByClass.append((t, summpg / vclasscount)) # append the tuple ('class', 'avg mpg')

HwyMpgByClass.sort(key=lambda x: x[1])
HwyMpgByClass

import datetime as dt
import time as tm

tm.time()

dtnow = dt.datetime.fromtimestamp(tm.time())
dtnow

dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second # get year, month, day, etc.from a datetime

delta = dt.timedelta(days = 100) # create a timedelta of 100 days
delta

today = dt.date.today()

today - delta # the date 100 days ago

today > today-delta # compare dates

class Person:
    department = 'School of Information' #a class variable

    def set_name(self, new_name): #a method
        self.name = new_name
    def set_location(self, new_location):
        self.location = new_location

person = Person()
person.set_name('Christopher Brooks')
person.set_location('Ann Arbor, MI, USA')
print('{} live in {} and works in the department {}'.format(person.name, person.location, person.department))

store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2)
cheapest

for item in cheapest:
    print(item)

my_function = lambda a, b, c : a + b

my_function(1, 2, 3)

my_list = []
for number in range(0, 1000):
    if number % 2 == 0:
        my_list.append(number)
my_list

my_list = [number for number in range(0,1000) if number % 2 == 0]
my_list

import numpy as np

mylist = [1, 2, 3]
x = np.array(mylist)
x

y = np.array([4, 5, 6])
y

m = np.array([[7, 8, 9], [10, 11, 12]])
m

m.shape

n = np.arange(0, 30, 2) # start at 0 count up by 2, stop before 30
n

n = n.reshape(3, 5) # reshape array to be 3x5
n

o = np.linspace(0, 4, 9) # return 9 evenly spaced values from 0 to 4
o

o.resize(3, 3)
o

np.ones((3, 2))

np.zeros((2, 3))

np.eye(3)

np.diag(y)

np.array([1, 2, 3] * 3)

np.repeat([1, 2, 3], 3)

p = np.ones([2, 3], int)
p

np.vstack([p, 2*p])

np.hstack([p, 2*p])

print(x + y) # elementwise addition     [1 2 3] + [4 5 6] = [5  7  9]
print(x - y) # elementwise subtraction  [1 2 3] - [4 5 6] = [-3 -3 -3]

print(x * y) # elementwise multiplication  [1 2 3] * [4 5 6] = [4  10  18]
print(x / y) # elementwise divison         [1 2 3] / [4 5 6] = [0.25  0.4  0.5]

print(x**2) # elementwise power  [1 2 3] ^2 =  [1 4 9]

x.dot(y) # dot product  1*4 + 2*5 + 3*6

z = np.array([y, y**2])
print(len(z)) # number of rows of array

z = np.array([y, y**2])
z

z.shape

z.T

z.T.shape

z.dtype

z = z.astype('f')
z.dtype

a = np.array([-4, -2, 1, 3, 5])

a.sum()

a.max()

a.min()

a.mean()

a.std()

a.argmax()

a.argmin()

s = np.arange(13)**2
s

s[0], s[4], s[-1]

s[1:5]

s[-4:]

s[-5::-2]

r = np.arange(36)
r.resize((6, 6))
r

r[2, 2]

r[3, 3:6]

r[:2, :-1]

r[-1, ::2]

r[r > 30]

r[r > 30] = 30
r

r2 = r[:3,:3]
r2

r2[:] = 0
r2

r

r_copy = r.copy()
r_copy

r_copy[:] = 10
print(r_copy, '\n')
print(r)

test = np.random.randint(0, 10, (4,3))
test

for row in test:
    print(row)

for i in range(len(test)):
    print(test[i])

for i, row in enumerate(test):
    print('row', i, 'is', row)

test2 = test**2
test2

for i, j in zip(test, test2):
    print(i,'+',j,'=',i+j)
