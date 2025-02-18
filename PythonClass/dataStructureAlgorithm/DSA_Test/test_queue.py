import unittest

from Dsa.queue import MyQueue

class TestMyQueue(unittest.TestCase):
    def setUp(self):
        self.queue = MyQueue()

    def test_that_queue_is_empty(self):
        self.assertTrue(self.queue.is_empty())

    def test_that_element_can_be_added_to_the_queue(self):
        self.assertTrue(self.queue.add("hello"))

    def test_that_element_index_can_be_found_from_the_queue(self):

        self.queue.add("hello")
        self.queue.add("world")
        self.queue.add("semicolon")
        self.queue.add("africa")
        self.assertEqual("semicolon", self.queue.elements())

    def test_that_element_can_be_removed_from_the_queue(self):
        self.queue.add("hello")
        self.queue.add("world")
        self.queue.add("semicolon")
        self.queue.remove("world")
        self.assertEqual(2, self.queue.size)

    def test_for_offer(self):
        self.queue.add("hello")
        self.queue.add("world")
        self.assertTrue(self.queue.is_offer())

    def test_for_poll(self):
        self.queue.add("hello")
        self.queue.add("world")
        self.queue.add("semicolon")
        self.assertEqual("hello", self.queue.poll())

if __name__ == '__main__':
    unittest.main()