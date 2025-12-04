# this single line comment
"""
Multiline comment
second
"""

n="Raghunath"
a=5
# boolian
b=True
c=False

print(a,len(n))
print(type(a))

# list
test_tuple=['hello', 'world', 34]

#  tuple
test_tuple=(2,'raghu', 'mahesh')

# Dict
test_dict = {'a': 1, 'b': 2}
print(test_dict)

# Set
# consider the values in an arbitrary way
test_set = {'a', 'b', "abc"}
print(test_set)

""" 
Operations
Add
Sub
Multi
Divide
Integer division
Modulo division
Addition  

"""

a = "42"
b = "43"
print(a + b) # Concatenation

# Power
a = 10
print(a**2) # a²

# Comparison operators
a = 10
b = 20
res = a > b
res_1 = a < b
res_2 = a != b
res_3 = a == b
print(res, res_1, res_2, res_3)

# Logical operators
# AND, NOT, OR
a = True
b = False

res = a and b
res_1 = a or b
res_2 = not a
res_3 = not b
print(res, res_1, res_2, res_3)