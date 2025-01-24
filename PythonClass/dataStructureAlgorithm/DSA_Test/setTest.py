import unittest

from DSA_Function.setFunction import setFunction

class setTest(unittest.TestCase):
    def test_that_sets_are_empty(self):
        set_test = setFunction()
        self.assertTrue(set_test.is_empty)

    def test_that_sets_are_not_empty(self):
        set_test = setFunction()
        set_test.add("stephen")
        set_test.add("hello")
        self.assertEqual(2, set_test.size)

    def test_that_sets_contain_hello(self):
        set_test = setFunction()
        set_test.add("stephen")
        set_test.add("hello")
        set_test.update("jame")
        self.assertEqual(3, set_test.size)

    def test_that_hello_can_be_removed(self):
        set_test = setFunction()
        set_test.add("stephen")
        set_test.add("hello")
        set_test.add("jame")
        set_test.remove("hello")
        self.assertEqual(2, set_test.size)

    def test_for_the_union_in_the_same_set(self):
        set_test = setFunction()
        set_test.add("stephen")
        set_test.add("hello")
        set_test.add("jame")
        set_test.add("hello")
        set_test.union("hello")
        self.assertEqual(3, set_test.size)
if __name__ == '__main__':
    unittest.main()