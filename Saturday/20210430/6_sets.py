## Join Two Sets

## union
## The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3, 'c'}
set3 = set1.union(set2)
print(set3)

## update
## The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3, 'c'}
set1.update(set2)
print(set1)

# Both union() and update() will exclude any duplicate items.

## Keep ONLY the Duplicates
## intersection
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

## intersection_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

## Keep All, But NOT the Duplicates
## symmetric_difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

## symmetric_difference_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)