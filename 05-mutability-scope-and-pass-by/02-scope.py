# Scope is a term to describe when and where variables are accessible
# in any given program at any given time. The complete details of scope
# can be complex, but for most situations we just need to understand
# Python's 2 main scopes: global and local.

# x is a global scope variable, because it is defined at the "top-level"
# of a file. Specifically we mean that it is defined outside any function.
x = 10

# Function parameters, such as y, belong to the local scope of the function
# that defines them. function_one in this case.
def function_one(y):
    # Variables defined in a function also belong to that function's local scope.
    z = y + 1

    # Global variables are accessible in every other scope.
    z += x

    # Global variables are also assignable in every other scope.
    x += z

# Micro-exercise: Predict what will happen for each of the following print statements.
function_one(20)
print(x)
print(y)
print(z)

