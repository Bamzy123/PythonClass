import unittest

from functions.diaries import Diaries
from functions.diary import Diary


class DiariesTest(unittest.TestCase):
    def test_can_add_and_find_diary(self):
        diaries = Diaries()

        first_diary_name = "Sam"
        first_diary_password = "passwordSam"
        second_diary_name = "Divine"
        second_diary_password = "passwordDivine"
        diary1 = Diary(first_diary_name, first_diary_password)
        diary2 = Diary(second_diary_name, second_diary_password)

        diaries.add_diary(diary1)
        diaries.add_diary(diary2)

        first_diary_name = "Sam"
        second_diary_name = "Divine"
        found_sam_diary = diaries.find_diary_by_username(first_diary_name)
        found_divine_diary = diaries.find_diary_by_username(second_diary_name)

        self.assertIsNotNone(found_sam_diary, "Diary for Sam should be found.")
        self.assertIsNotNone(found_divine_diary, "Diary for Divine should be found.")
        self.assertEqual(first_diary_name, found_sam_diary.get_username())
        self.assertEqual(second_diary_name, found_divine_diary.get_username())

    def test_finding_non_existent_diary_returns_none(self):
        diaries = Diaries()

        first_diary_name = "Sam"
        first_diary_password = "passwordSam"

        diary1 = Diary(first_diary_name, first_diary_password)
        diaries.add_diary(diary1)

        self.assertIsNone(diaries.find_diary_by_username("Esther"),
                          "Should return None for a non-existent diary.")

    def test_can_delete_diary(self):
        diaries = Diaries()

        first_diary_name = "Sam"
        first_diary_password = "passwordSam"
        second_diary_name = "Divine"
        second_diary_password = "passwordDivine"
        diary1 = Diary(first_diary_name, first_diary_password)
        diary2 = Diary(second_diary_name, second_diary_password)
        diaries.add_diary(diary1)
        diaries.add_diary(diary2)

        diaries.delete_diary(diary1)

        self.assertIsNone(diaries.find_diary_by_username(diary1),
                          "Sam's diary should be deleted.")
        self.assertIsNotNone(diaries.find_diary_by_username(diary2.get_username()),
                             "Divine's diary should still be present.")

if __name__ == '__main__':
    unittest.main()