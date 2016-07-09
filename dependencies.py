# Highly coupled code is code where the dependencies between classes are dense,
# lots of things depend on other things, leading to a difficult-to-understand, maintain
# and easy-to-break program. Simplistically, we can say that class A is statically coupled
# to class B if the compiler needs the definition of B in order to compile class A.
# Moreover the dependencies among them are transitive: if A depends on B and B depends
# on C, then A depends on C.
# Create an algorithm which can print the expanded dependency tree given a set of class
# dependencies. Make sure there are no duplicates in the output.


def get_dependencies():
    graph = {'A': ['B', 'C', 'E', 'F', 'G', 'H'], 'B': ['C', 'E', 'F', 'G', 'H'], 'C': ['G'], 'D': ['A', 'B', 'C', 'E', 'F', 'G', 'H'], 'E': ['F', 'H'], 'F': ['H']}
