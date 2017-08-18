from collections import OrderedDict, deque
from copy import copy, deepcopy


class Vertex(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __hash__(self):
        return hash((self.name, self.weight))

    def __str__(self):
        return '(' + self.name + ',' + str(self.weight) + ')'

    def __repr__(self):
        return '(' + self.name + ',' + str(self.weight) + ')'


class DAGraph(object):
    def __init__(self):
        """ Construct a new DAGraph with no vertices or edges. """
        self.reset_graph()

    def has_vertex(self, vertex):
        for k in self.graph:
            if k.name == vertex.name:
                return True
        return False

    def add_vertex(self, vertex, graph=None):
        """ Add a vertex if it does not exist yet, or error out. """
        if not graph:
            graph = self.graph
        if self.has_vertex(vertex):
            raise KeyError('vertex %s already exists' % vertex_name)
        graph[vertex] = set()

    def add_edge(self, ind_vertex, dep_vertex, graph=None):
        if not graph:
            graph = self.graph
        if ind_vertex not in graph or dep_vertex not in graph:
            raise KeyError('one or more vertices do not exist in graph')
        test_graph = deepcopy(graph)
        test_graph[ind_vertex].add(dep_vertex)
        is_valid, message = self.validate(test_graph)
        if is_valid:
            graph[ind_vertex].add(dep_vertex)

    def ind_vertices(self, graph=None):
        """ Returns a list of all vertices in the graph with no dependencies. """
        if graph is None:
            graph = self.graph

        dependent_vertices = set(vertex for dependents in graph.values() for vertex in dependents)
        return [vertex for vertex in graph.keys() if vertex not in dependent_vertices]

    def validate(self, graph=None):
        graph = graph if graph is not None else self.graph
        if len(self.ind_vertices(graph)) == 0:
            return False, 'no independent vertices detected'
        try:
            self.topological_sort(graph)
        except ValueError:
            return False, 'failed topological sort'
        return True, 'valid'

    def topological_sort(self, graph=None):
        """ Returns a topological ordering of the DAGraph.
        Raises an error if this is not possible (graph is not valid).
        """
        if graph is None:
            graph = self.graph

        in_degree = {}
        for u in graph:
            in_degree[u] = 0

        for u in graph:
            for v in graph[u]:
                in_degree[v] += 1

        queue = deque()
        for u in in_degree:
            if in_degree[u] == 0:
                queue.appendleft(u)

        l = []
        while queue:
            u = queue.pop()
            l.append(u)
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.appendleft(v)

        if len(l) == len(graph):
            return l
        else:
            raise ValueError('graph is not acyclic')

    def find_all_paths(self, start, path=[]):
        path = path + [start]
        if start not in self.graph:
            return []

        if len(self.graph[start]) == 0:
            return [path]

        paths = []
        for vertex in self.graph[start]:
            if vertex not in path:
                new_paths = self.find_all_paths(vertex, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths
    """
    Function code

    """
    def find_optimal_path(self, start):
        all_paths = self.find_all_paths(start)
        sum_weights = 0
        optimal_path = []
        for path in all_paths:
            current_sum = sum(v.weight for v in path)
            if current_sum > sum_weights:
                sum_weights = current_sum
                optimal_path = path
        return optimal_path

    """
        Time complexity : O(ve), v is the number of vertices, e is the number of edges
    """

    def reset_graph(self):
        self.graph = OrderedDict()

"""
    Test Code
"""
import unittest


class TestFlattenMethods(unittest.TestCase):
    def test_the_example(self):
        a = Vertex("A", 1)
        b = Vertex("B", 2)
        c = Vertex("C", 2)
        g = DAGraph()
        g.add_vertex(a)
        g.add_vertex(b)
        g.add_vertex(c)
        g.add_edge(a, b)
        g.add_edge(b, c)
        g.add_edge(a, c)
        r = g.find_optimal_path(a)
        er = [a, b, c]
        self.assertEqual(r, er)

    def test_second(self):
        a = Vertex("A", 1)
        b = Vertex("B", 2)
        c = Vertex("C", 3)
        d = Vertex("D", 4)
        e = Vertex("E", 5)
        g = DAGraph()
        g.add_vertex(a)
        g.add_vertex(b)
        g.add_vertex(c)
        g.add_vertex(d)
        g.add_vertex(e)
        g.add_edge(a, b)
        g.add_edge(b, c)
        g.add_edge(b, d)
        g.add_edge(d, e)
        g.add_edge(c, e)
        r = g.find_optimal_path(a)
        er = [a, b, d, e]
        self.assertEqual(r, er)

if __name__ == '__main__':
    unittest.main()


"""
Bonus : If the graph is cyclic (don't call validate method), to avoid infinite loop, we only visit the vertex
if it's not in the path.
The condition to stop is the vertex has no neighbours that doesn't belong to the path:
    len([v for v in self.graph[start] if v not in path]) == 0:

"""