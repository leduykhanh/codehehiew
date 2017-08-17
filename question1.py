"""
    Function code
"""
def flatten_dict(input_dict):
    def flatten_dict_generator(py_dict, key_string=''):
        """
        :param py_dict: the input dictionary
        :param key_string: for the recursive
        :return: the key:value of the lowest level
        """
        if type(py_dict) is dict:
            key_string = key_string + "." if key_string else key_string
            for k in py_dict:
                yield from flatten_dict_generator(py_dict[k], key_string + k)
        else:
            yield key_string, py_dict
    return {k: v for k, v in flatten_dict_generator(input_dict)}
"""
    Time complexity : O(n), n is the number of keys
"""

"""
    Test Code
"""
import unittest


class TestFlattenMethods(unittest.TestCase):
    def test_two_levels(self):
        depth_one = {'a': 1, 'b': {'a': 2, 'b': {'x': 5, 'y': 10}}, 'd': [1, 2, 3]}
        result = {'d': [1, 2, 3], 'b.a': 2, 'b.b.y': 10, 'a': 1, 'b.b.x': 5}
        self.assertEqual(flatten_dict(depth_one), result)

    def test_given_example(self):
        m = {"a": 1, "b": {"c": 2, "d": [3, 4]}}
        o = {"a": 1, "b.c": 2, "b.d": [3, 4]}
        r = flatten_dict(m)
        self.assertEqual(r, o)


if __name__ == '__main__':
    unittest.main()
