import unittest
from movie_rating_functions.movie_rating import Movie, MovieNotFoundError, InvalidRatingError, MovieAlreadyExistsError
from datetime import datetime

class TestMovie(unittest.TestCase):
    def setUp(self):
        self.movie = Movie()

    def test_movie_can_be_added_and_with_timestamp(self):
        self.movie.add_movie("Koko_iye")
        self.assertIn("Koko_iye", self.movie.movies)
        self.assertIsInstance(self.movie.movies["Koko_iye"]["added_on"], datetime)

    def test_that_movie_title_cannot_repeat_itself(self):
        self.movie.add_movie("Koko_iye")
        with self.assertRaises(MovieAlreadyExistsError):
            self.movie.add_movie("Koko_iye")

    def test_for_movie_rating(self):
        self.movie.add_movie("Koko_iye")
        self.assertEqual(self.movie.movie_rating("Koko_iye", 5), 5.0)
        self.assertEqual(self.movie.movie_rating("Koko_iye", 3), 4.0)

    def test_exception_for_invalid_movie(self):
        with self.assertRaises(MovieNotFoundError):
            self.movie.movie_rating("NonExistent", 5)

    def test_that_movie_rating_must_be_btw_one_too_five(self):
        self.movie.add_movie("Koko_iye")
        with self.assertRaises(InvalidRatingError):
            self.movie.movie_rating("Koko_iye", 6)

    def test_to_get_average_rating_for_a_movie(self):
        self.movie.add_movie("Spy_Kid")
        self.movie.movie_rating("Spy_Kid", 4)
        self.movie.movie_rating("Spy_Kid", 2)
        self.assertEqual(self.movie.get_average_rating("Spy_Kid"), 3.0)

    def test_that_to_get_average_rating_for_invalid_movie_should_raise_an_exception(self):
        with self.assertRaises(MovieNotFoundError):
            self.movie.get_average_rating("NonExistent")

    def test_to_get_overall_average_rating_of_all_movies_in_the_application(self):
        self.movie.add_movie("Koko_iye")
        self.movie.add_movie("Spy_Kid")
        self.movie.movie_rating("Koko_iye", 5)
        self.movie.movie_rating("Koko_iye", 3)
        self.movie.movie_rating("Spy_Kid", 4)
        self.movie.movie_rating("Spy_Kid", 2)
        self.assertEqual(self.movie.get_overall_average_rating(), 3.5)

    def test_to_get_overall_average_rating_with_no_ratings_input_in_the_application(self):
        self.assertIsNone(self.movie.get_overall_average_rating())

    def test_to_view_all_movies_in_the_application(self):
        self.movie.add_movie("Koko_iye")
        self.movie.add_movie("Spy_Kid")
        self.movie.view_all_movies()
        all_movies = self.movie.view_all_movies()
        self.assertEqual(len(all_movies), 2)
if __name__ == '__main__':
    unittest.main()