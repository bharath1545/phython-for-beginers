# union is a mathematical operation that combines the elements of two sets, resulting in a new set that contains all unique elements from both sets. In Python, you can perform a union operation on sets using the `union()` method or the `|` operator.
# The union of two sets A and B is denoted as A ∪ B, and it includes all elements that are in A, in B, or in both. Duplicate elements are automatically removed in the resulting set.
s1={1,45,6}
s2={7,8,1}
print(s1.union(s2)) # Using the union() method to combine s1 and s2
print(s1.intersection(s2)) # Using the intersection() method to find common elements between s1 and s2