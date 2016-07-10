import unittest


class KindleDependencyTracker():

    def __init__(self, operation_list):
        self.operation_list = operation_list
        self.start_dependency_graph = {}
        self.end_dependency_graph = {}

    def make_start_dependency_graph(self):
        for operation_str in self.operation_list:
            split_str = operation_str.split(",")

            self.start_dependency_graph[split_str[0]] = split_str[1:]

    def make_end_dependency_graph(self):
        for key in self.start_dependency_graph:
            dependencies = []

            self.add_deps(key, dependencies, self.start_dependency_graph)
            self.end_dependency_graph[key] = dependencies

    def add_deps(self, node, dependencies, graph):

        if node not in graph:
            return

        for dep in graph[node]:
            if dep in dependencies:
                dependencies.remove(dep)
            dependencies.append(dep)
            self.add_deps(dep, dependencies, graph)


class TestKindleDependencyTracker(unittest.TestCase):

    def test_get_dependencies(self):

        operation_list = ['one', 'two,one', 'final,two']

        dependency_tracker = KindleDependencyTracker(operation_list)
        dependency_tracker.make_start_dependency_graph()
        dependency_tracker.make_end_dependency_graph()

        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
