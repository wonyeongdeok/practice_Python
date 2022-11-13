a = ['gsw', 'lakers', 'clippers']
b = [1, 2, 3]

dict(zip(a, b))

x = ['car', 'truck', 'bus']
y = [10, 20, 30]

zipped = list(zip(x, y))
zipped

x, y = zip(*zipped)
x
y
list(x)

flst = [[1,2,3], [8,9,12,17], [3,7]]
sorted(sum(flst, []))

import pandas as pd

df = pd.DataFrame({'Name': ['Bob', 'John', 'Foo', 'Bar', 'Alex', 'Tom'],
                    'Math': ['A+', 'B', 'A', 'F', 'D', 'C'],
                    'English': ['C', 'B', 'B', 'A+', 'F', 'A'],
                    'Age': [13, 16, 16, 15, 15, 113]})
df
df1 = df.melt(id_vars=['Name', 'Age'])
df1



from faker import Faker
fake = Faker()
name = fake.name()
name
address = fake.address()
address
text = fake.text()
text




df = pd.DataFrame({'Location': ['Cupertino', 'Los Angles, California', 'Palo Alto, California']})
df


df[['City', 'State']] = df.Location.str.split(',', expand=True)
df



reverse = [1,2,3,4,8,9]
reverse
reverse[::-1]

x = 5
y = 10
x, y = y, x
x
y

a = {'apple': 2}
b = {'apple': 2, 'orange': 2, 'banana': 3}
{**a, **b}

 print("\N{SMILING FACE WITH HALO}")
  print("\N{thinking face}")

 a, b, c = [1, 2, 3]
print(a, b, c)

*a, b, c = [1, 2, 3, 4, 5, 6]
print(a, b, c)
type(a)
type(b)

a, *b, c = [1, 2, 3, 4, 5,  6]
print(a, b, c)


l1 = ['a','b','c','d','e','f','g','h','a','b']
l2 = ['e','f','g','h','i','j']

s1 = set(l1).intersection(l2)
s1
list(s1)



# Append a value to the list-

l1 = ['apple', 'oranges','bananas']
l1.append('grapes')
l1

# Append a list - use concatenate
c1 = ['apple', 'oranges','bananas']
c1 = c1 + ['grapes']
c1

#remove a sublist from a list-use remove method
l1 = [10,20,30,40,50,60]
s1 = [30,40,50]
for i in s1:
  l1.remove(i)
print(l1)

#use negative index . If you get confused then use [~0] for [-1]
l1 = l1 = [10,20,30,40,50,60]
print(l1[-1])
print(l1[-2])
print(l1[~0])
print(l1[~1])


# Use Slice Assignment
l1 = [10,20,30,40,50,60,70,80,90]

#Replace
l1[1:3] = [21,31]
l1
#[10, 21, 31, 40, 50, 60, 70, 80, 90]
#Delete
l1[1:3] = []
l1
#[10, 40, 50, 60, 70, 80, 90]
#Add
l1[1:1] = [10,20,30]
l1
#[10, 10, 20, 30, 40, 50, 60, 70, 80, 90]

import keyword
a = keyword.kwlist

type(a[1])
a

dir(__builtins__)

help(print)

dir(pd)
help(pd.util)


l1 = [10,20,30,40,50,60,70,80]
l1.pop(2)

l1.reverse()
l1

#check if the element exists in the list.
l1 = ['sanjose', 'cupertino', 'sunnyvale', 'fremont']
'sanjose' in l1
#Returns True
'paloalto' in l1
#returns False


 #Any or All
l1 = ['sanjose', 'cupertino', 'sunnyvale', 'fremont']
all(l1)
#Rreturns True

l2= [0,0,0,False,1]
any(l2)
#Returns False


import heapq
numbers = [10, 40, 25, 500, 90, 59, 320, 200, 100, 800]
print(heapq.nlargest(4, numbers))

import heapq
numbers = [10, 40, 25, 500, 90, 59, 320, 200, 100, 800]
print(heapq.nsmallest(4, numbers))

from os.path import exists
file_exists = exists("/content/sample_data/california_housing_test.csv")
print(file_exists)
#True

from pathlib import Path
path = Path("/content/sample_data/california_housing_test.csv")
path.is_file()
#False
import os
def is_empty_file(fpath):
  return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

fp="/content/sample_data/california_housing_test.csv"

is_empty_file(fp)


def func(*args):
# args will be a tuple containing all values that are passed in
  for i in args:
    print(i)
func(200,400,500,700) # Calling it with 4 arguments

def func(**kwargs):
# kwargs will be a dictionary containing the names as keys and the values as values
  for name, value in kwargs.items():
    print(name,':', value)
dict1={'apple': 1, 'orange': 2,'grapes': 2 }
func(**dict1)

#The lambda keyword creates an inline function that contains a single expression. The value of this expression is what the function returns when invoked.
#Use it inside a function
def transform(n):
  return lambda x: x + n

f = transform(3)
f(4)

#7

#simple lambda function
lambda x: x**2 + 2*x - 5

#Lamda
a = lambda x: x**2 + 2*x - 5
a(1)

#regular function
def a(x): return x + 1
a(1)
