# Highly coupled code is code where the dependencies between classes are dense,
# lots of things depend on other things, leading to a difficult-to-understand, maintain
# and easy-to-break program. Simplistically, we can say that class A is statically coupled
# to class B if the compiler needs the definition of B in order to compile class A.
# Moreover the dependencies among them are transitive: if A depends on B and B depends
# on C, then A depends on C.
# Create an algorithm which can print the expanded dependency tree given a set of class
# dependencies. Make sure there are no duplicates in the output.


def get_dependencies(node, dependencies, graph):
    # base case
    if node not in graph:
        return
    for dependency in graph[node]:
        # add new node to set
        dependencies.add(dependency)
        get_dependencies(dependency, dependencies, graph)


def build_dependencies(graph):
    dependency_graph = {}

    for key in graph:
        dependency_graph[key] = set()
        get_dependencies(key)

    return dependency_graph

print build_dependencies({'A': ['B', 'C'], 'B': ['C', 'E'], 'C': ['G'], 'D': ['A', 'F'], 'E': ['F'], 'F': ['H']})
