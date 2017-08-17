"""
    Function code
"""
def store_array(array):
    if type(array) is not list:
        return ''
    array_of_string = []
    for array_item in array:
        if type(array_item) is dict:
            string_rep = ';'.join([k + '=' + v for k,v in array_item.items()])
            array_of_string.append(string_rep)
    output = '\n'.join(array_of_string)
    return output


def load_array(string):
    result_array = []
    for string_item in string.split('\n'):
        dict_item = {}
        for dict_string in string_item.split(';'):
            k_v_pair =  dict_string.split('=')
            try:
                dict_item[k_v_pair[0]] = k_v_pair[1]
            except:
                return []
        result_array.append(dict_item)
    return result_array

"""
    Time complexity : O(n), n is the total number of keys in the array
"""

"""
    Test Code
"""
import unittest


class TestFlattenMethods(unittest.TestCase):
    def test_store(self):
        a = [{"a": "A", "b": "B"}, {"c": "C"}]
        result = 'a=A;b=B\nc=C'
        self.assertEqual(store_array(a), result)

    def test_load(self):
        a = [{"a": "A", "b": "B"}, {"c": "C"}]
        result = 'a=A;b=B\nc=C'
        r = load_array(result)
        self.assertEqual(r, a)


if __name__ == '__main__':
    unittest.main()