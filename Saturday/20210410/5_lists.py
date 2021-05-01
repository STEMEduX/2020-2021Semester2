## Sort
## string
thislist = ["orange", "mango", "kiwi", "pineapple", "basket", "banana", "kiwi" ]
thislist.sort()
print(thislist)

## number
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

## descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

pointA = (0, 0)
pointB = (0, 1)
print(pointA > pointB)
print(pointB > pointA)
## customized sort function
def myfunc(n):
  return abs(n)

thislist = [100, -50, 65, -82, 23]
thislist.sort() # sort by its absolute value
print(thislist)
thislist.sort(key = myfunc)
print(thislist)

def distance(point): # point is a tuple (x, y)
    return point[0]**2 + point[1]**2 ## sqrt(x^2 + y^2) 

thislist = [(0, 0), (0,10), (2, 2)]
thislist.sort()
print(thislist)
thislist.sort(key=distance)
print(thislist)

## case insensitive
## ASCII, compare 2 char, compare ASCII code.
## ASCII, uppercase before lowercase
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
thislist.sort(key = str.lower)
print(thislist)
thislist.sort(key = str.upper)
print(thislist)

## reverse order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
thislist = [2, 1, 8, 9, 7]
thislist.reverse()
print(thislist)

# elelemt should be comparable
# string vs string, python know to compare it
# int, int
# string, int, error, python does not know how to compare.
thislist = ['a', 'abc', 1, 2, 'xyz', 3, 'kkkk', 10000, '0abc', 9900]
# thislist.sort() # error out.
def my_compare_func(n): # input -> str
  return str(n)
thislist.sort(key=my_compare_func)
print(thislist) 

# '1', '10000'. '2'
# '1000' vs '1' 49 == 49, nothing < 48   
# '1' , '2'=> 49 < 50
# '10000', '2' 49 < 50 compare first 
# # 'a', 'b' => ascii code
# '10000' vs 'xyz' => 49 < 120
# 'a' vs 'A' => 97 > 65 'A', 'a'