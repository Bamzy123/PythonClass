import unittest

from Dsa.stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_stack_is_empty(self):
        self.assertTrue(self.stack.is_empty(), "Stack should be empty initially.")

    def test_push_increases_size(self):
        self.stack.push(10)
        self.assertFalse(self.stack.is_empty(), "Stack should not be empty after pushing an element.")
        self.assertEqual(self.stack.size(), 1, "Stack size should be 1 after one push.")

    def test_pop_returns_last_item(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3, "Popped element should be the last pushed element (3).")
        self.assertEqual(self.stack.pop(), 2, "Popped element should be the next element (2).")
        self.assertEqual(self.stack.pop(), 1, "Popped element should be the first pushed element (1).")

    def test_peek_returns_last_item_without_removing(self):
        self.stack.push("a")
        self.stack.push("b")
        top = self.stack.peek()
        self.assertEqual(top, "b", "Peek should return the last pushed element (b).")
        self.assertEqual(self.stack.size(), 2, "Stack size should remain unchanged after peek.")

    def test_pop_on_empty_stack_raises_exception(self):
        with self.assertRaises(Exception, msg = "Popping an empty stack should raise an exception."):
            self.stack.pop()

    def test_peek_on_empty_stack_raises_exception(self):
        with self.assertRaises(Exception, msg = "Peeking an empty stack should raise an exception."):
            self.stack.peek()

if __name__ == '__main__':
    unittest.main()

