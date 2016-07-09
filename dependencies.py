# Highly coupled code is code where the dependencies between classes are dense,
# lots of things depend on other things, leading to a difficult-to-understand, maintain
# and easy-to-break program. Simplistically, we can say that class A is statically coupled
# to class B if the compiler needs the definition of B in order to compile class A.
# Moreover the dependencies among them are transitive: if A depends on B and B depends
# on C, then A depends on C.
# Create an algorithm which can print the expanded dependency tree given a set of class
# dependencies. Make sure there are no duplicates in the output.


def get_dependencies(node_list):
    graph = {'A': ['B', 'C'], 'B': ['C', 'E'], 'C': ['G'], 'D': ['A', 'F'], 'E': ['F'], 'F': ['H']}

    dependencies = []
    for item in node_list:
        for val in graph[item]:
            dependencies.append(val)

    print dependencies

print get_dependencies(['A', 'B', 'C'])
