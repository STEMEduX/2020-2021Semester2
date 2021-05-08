## Join Two Sets

## union
## The union() method returns a new set with all items from both sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3, 'c'}
set3 = set1.union(set2)
print(set3)
print(set1)
print(set2)

print('------')
## update
## The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3, 'c'}
set1.update(set2)
print(set1)
print(set2)

# Both union() and update() will exclude any duplicate items.

## Keep ONLY the Duplicates
## intersection
print('------')
x = {"apple", "banana", "cherry", "A"}
y = {"google", "microsoft", "apple", "A"}
print('this is ', x.isdisjoint(y))
z = x.intersection(y)
print(z)

print('------')
## intersection_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

print('------')
## Keep All, But NOT the Duplicates
## symmetric_difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

print('------')
## symmetric_difference_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

print('----')
sub = { 1, 2, 3}
superset = { 1, 2, 3, 4, 5}
sameset = {1,2,3}
print('sub set', sub.issubset(superset))
print('super set', superset.issuperset(sub))
print('sub set', sub.issubset(sameset))
print('super set', sub.issuperset(sameset))
