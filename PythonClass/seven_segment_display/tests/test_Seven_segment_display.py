import unittest

from seven_segment.seven_segment import get_seven_segment_display

class TestSevenSegmentDisplay(unittest.TestCase):

    def test_segment8(self):
        expected = [
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        actual = get_seven_segment_display(8)
        self.assertEqual(len(expected), len(actual))
        for index in range(len(expected)):
            self.assertEqual(expected[index], actual[index])

    def test_segment1(self):
        expected = [
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', '#'],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', '#'],
            [' ', ' ', ' ', ' ']
        ]
        actual = get_seven_segment_display(1)
        self.assertEqual(len(expected), len(actual))
        for index in range(len(expected)):
            self.assertEqual(expected[index], actual[index])

    def test_segment2(self):
        expected = [
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', ' '],
            ['#', '#', '#', '#']
        ]
        actual = get_seven_segment_display(2)
        self.assertEqual(len(expected), len(actual))
        for index in range(len(expected)):
            self.assertEqual(expected[index], actual[index])

    def test_segment3(self):
        expected = [
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        actual = get_seven_segment_display(3)
        self.assertEqual(len(expected), len(actual))
        for index in range(len(expected)):
            self.assertEqual(expected[index], actual[index])

    def test_segment4(self):
        expected = [
            [' ', ' ', ' ', ' '],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            [' ', ' ', ' ', ' ']
        ]
        actual = get_seven_segment_display(4)
        self.assertEqual(len(expected), len(actual))
        for index in range(len(expected)):
            self.assertEqual(expected[index], actual[index])

    def test_segment5(self):
        expected = [
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', ' '],
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        actual = get_seven_segment_display(5)
        self.assertEqual(len(expected), len(actual))
        for index in range(len(expected)):
            self.assertEqual(expected[index], actual[index])

    def test_segment6(self):
        expected = [
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', ' '],
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        actual = get_seven_segment_display(6)
        self.assertEqual(len(expected), len(actual))
        for index in range(len(expected)):
            self.assertEqual(expected[index], actual[index])

    def test_segment7(self):
        expected = [
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', '#'],
            [' ', ' ', ' ', '#']
        ]
        actual = get_seven_segment_display(7)
        self.assertEqual(len(expected), len(actual))
        for index in range(len(expected)):
            self.assertEqual(expected[index], actual[index])

    def test_segment9(self):
        expected = [
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        actual = get_seven_segment_display(9)
        self.assertEqual(len(expected), len(actual))
        for index in range(len(expected)):
            self.assertEqual(expected[index], actual[index])

if __name__ == '__main__':
    unittest.main()
