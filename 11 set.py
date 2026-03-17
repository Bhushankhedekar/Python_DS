# Set details
# A set is an unordered collection of unique items.
# Sets are mutable, which means that you can add or remove items from a set after it has been created.
# if we want unique data then we can use set because set does not allow duplicate data

s1 = {1, 2, 3, 4, 5}
for data in s1:
    print(data)

#find second max element from data
# marks = [10, 10, 20, 30, 40, 50, 20, 20, 10, 99, -99, -99, 88, 88 ,100 ,100, 60, 70, 80, 90, 100] 
# unique_marks = list(set(marks))
# unique_marks.sort(reverse=True)
# print("Second max element:", unique_marks[1])

# Set methods
# 1. add() : adds an element to the set
s2 = {1, 2, 3, 4, 5}
s2.add(6)
print("Set after adding an element: ", s2)

# 2. remove() : removes an element from the set
s2.remove(6)
print("Set after removing an element: ", s2)

# 3. discard() : removes an element from the set if it is present, otherwise
# does nothing
s2.discard(6)
print("Set after discarding an element: ", s2)

# 4. pop() : removes and returns an arbitrary element from the set
s2.pop()
print("Set after popping an element: ", s2)

# 5. clear() : removes all the elements from the set
s2.clear()
print("Set after clearing all elements: ", s2)

# 6. union() : returns a new set that is the union of two sets
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = s1.union(s2)
print("Union: ", s3)
print("union operator: ", s1 | s2)

# 7. intersection() : returns a new set that is the intersection of two sets
s4 = s1.intersection(s2)
print("Intersection: ", s4)
print("intersection operator: ", s1 & s2)

# 8. difference() : returns a new set that is the difference of two sets
s5 = s1.difference(s2)
print("Difference: ", s5)
print("difference operator: ", s1 - s2)

# 9. symmetric_difference() : returns a new set that is the symmetric difference
# of two sets
s6 = s1.symmetric_difference(s2)
print("Symmetric Difference: ", s6)
print("symmetric difference operator: ", s1 ^ s2)


marks = [88,99,99,88,77,66,55,44,33,22,11,0,-99,-90,45,55,76,78,98,34,43,56,76,7,92,32]
topper = marks[0]
for m in marks:
    if m > topper:
        topper = m
print("Topper marks: ", topper)

m2 = sorted(marks)
print("Second topper marks: ", m2[-2])

