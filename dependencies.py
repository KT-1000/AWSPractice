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
        if dependency in dependencies:
            dependencies.remove(dependency)
        # add new node
        dependencies.append(dependency)
        get_dependencies(dependency, dependencies, graph)


def build_dependencies(graph):
    dependency_graph = {}

    for key in graph:
        dependency_graph[key] = []
        get_dependencies(key, dependency_graph[key], graph)

    return dependency_graph


def get_max_key(graph):
    max_length = 0
    max_key = ""

    for key in graph:
        key_len = len(graph[key])

        if key_len > max_length:
            max_length = key_len
            max_key = key

    return max_key


def print_instruction(key):
    "Operation " + key + " on part X"


def print_instructions(key, graph):
    max_deps = graph[key]

    max_deps.reverse()

    for dep in max_deps:
        print print_instruction(dep)

    print print_instruction(key)

max_key = get_max_key(graph)
print_instructions(max_key, graph)

print build_dependencies({
    'one': [],
    'two': ['one'],
    'final': ['two']
})

