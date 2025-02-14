import unittest

from Dsa.array import Array


class TestArray(unittest.TestCase):

    def setUp(self):
        self.array_test = Array(5)

    def test_isEmpty_initial(self):
        self.assertTrue(self.array_test.isEmpty())

    def test_isFull_initial(self):
        self.assertFalse(self.array_test.isFull())

    def test_append(self):
        self.assertFalse(self.array_test.append(10))
        self.assertFalse(self.array_test.append(20))
        self.assertFalse(self.array_test.append(30))
        self.assertFalse(self.array_test.append(40))
        self.assertTrue(self.array_test.append(50))

    def test_remove(self):
        self.array_test.append(10)
        self.array_test.append(20)
        self.array_test.remove(10)
        self.assertFalse(10 in self.array_test.my_list)
        self.assertEqual(self.array_test.size, 1)

        with self.assertRaises(TypeError):
            self.array_test.remove(100)

    def test_pop(self):
        self.array_test.append(10)
        self.array_test.append(20)
        popped_value = self.array_test.pop(1)
        self.assertEqual(popped_value, 20)
        self.assertEqual(self.array_test.size, 1)

        self.assertFalse(self.array_test.pop(10))

    def test_insert(self):
        self.array_test.append(10)
        self.array_test.append(20)
        self.assertTrue(self.array_test.insert(1, 15))
        self.assertEqual(self.array_test.my_list[1], 15)

        self.assertFalse(self.array_test.insert(10, 25))

    def test_size_and_capacity(self):
        self.array_test.append(10)
        self.assertEqual(self.array_test.size, 1)
        self.assertEqual(self.array_test.capacity, 5)

    def test_combination(self):
        self.array_test.append(10)
        self.array_test.append(20)
        self.array_test.append(30)
        self.array_test.remove(20)
        self.array_test.insert(1, 25)
        self.array_test.pop(0)
        self.assertEqual(self.array_test.my_list, [25, 30])


if __name__ == '__main__':
    unittest.main()