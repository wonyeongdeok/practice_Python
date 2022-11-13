abs(3)
abs(-3)
abs(-1.2)

all([1,2,3])
all([1,2,3,0])
all([])

any([1,2,3,0])
any([0, ""])

chr(97)
chr(44032)

dir([1,2,3])

divmod(7,3)

eval('1+2')
eval("'hi' + 'a'")
eval('divmod(4,3)')

def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1, -3, 2, 0, -5, 6]))

def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))


list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))

hex(234)
hex(3)

a = 3
id(3)
id(a)
b = a
id(b)

class Person : pass
a = Person()
isinstance(a, Person)

b = 3
isinstance(b, Person)

def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)

def two_times(x):
    return x*2

list(map(two_times, [1,2,3,4]))
list(map(lambda a: a*2, [1,2,3,4]))

max([1,2,3])
max('python')

oct(34)
oct(12345)


ord('a')
ord('가')

pow(2, 4)
pow(3, 3)

list(range(5))
list(range(5,10))
list(range(1,10,2))
list(range(0,-10,-1))
round(4.6)
round(4.2)
round(5.678, 2)

sorted([3,1,2])
sorted(['a', 'c', 'b'])
sorted('zero')
sorted((3,2,1))

tuple('abc')
tuple([1,2,3])
tuple((1,2,3))

list(zip([1,2,3], [4,5,6]))
list(zip([1,2,3], [4,5,6], [7,8,9]))
list(zip('abc', 'def'))
