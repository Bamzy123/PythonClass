from unittest import TestCase

from rotate import can_rotate


class Test(TestCase):
    def test_can_rotate_abcde_cdead(self):
        self.assertTrue(can_rotate("abcde", "cdeab"))

    def test_can_rotate_cba_abc(self):
        self.assertFalse(can_rotate("cba", "abc"))

    def test_can_rotate_13456_45612(self):
        self.assertTrue(can_rotate("13456", "45613"))