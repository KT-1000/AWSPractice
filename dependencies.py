# Highly coupled code is code where the dependencies between classes are dense,
# lots of things depend on other things, leading to a difficult-to-understand, maintain
# and easy-to-break program. Simplistically, we can say that class A is statically coupled
# to class B if the compiler needs the definition of B in order to compile class A.
# Moreover the dependencies among them are transitive: if A depends on B and B depends
# on C, then A depends on C.
# Create an algorithm which can print the expanded dependency tree given a set of class
# dependencies. Make sure there are no duplicates in the output.


def add_depths(node, dependencies, graph):
    for val in node:
        dependencies[node].add(val)


def get_dependencies(graph):
    dependencies = {}

    for key in graph:
        dependencies[key] = set()

        for item in graph[key]:
            # add the dependencies to that node's set
            dependencies[key].add(item)
            # the item is also a node, so go get the items in that node's value list if they exist
            if item in graph:
                add_depths(graph[item], dependencies, graph)

    return dependencies

print get_dependencies({'A': ['B', 'C'], 'B': ['C', 'E'], 'C': ['G'], 'D': ['A', 'F'], 'E': ['F'], 'F': ['H']})
