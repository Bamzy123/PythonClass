from datetime import datetime
from movie_rating_functions.exceptions import MovieNotFoundError
from movie_rating_functions.exceptions import InvalidRatingError
from movie_rating_functions.exceptions import MovieAlreadyExistsError

class Movie:
    def __init__(self):
        self.movies = {}

    def add_movie(self, name):
        if name in self.movies:
            raise MovieAlreadyExistsError(f"The movie '{name}' already exists.")
        self.movies[name] = {"ratings": [], "added_on": datetime.now()}
        return True

    def movie_rating(self, name, rating):
        if name not in self.movies:
            raise MovieNotFoundError(f"Movie '{name}' not found.")
        if not (1 <= rating <= 5):
            raise InvalidRatingError("Rating must be between 1 and 5.")

        self.movies[name]["ratings"].append(rating)
        return sum(self.movies[name]["ratings"]) / len(self.movies[name]["ratings"])

    def get_average_rating(self, name):
        if name not in self.movies:
            raise MovieNotFoundError(f"Movie '{name}' not found.")
        if not self.movies[name]["ratings"]:
            return None
        return sum(self.movies[name]["ratings"]) / len(self.movies[name]["ratings"])

    def get_overall_average_rating(self):
        total_ratings = []
        for movie in self.movies.values():
            total_ratings.extend(movie["ratings"])

        if not total_ratings:
            return None

        return sum(total_ratings) / len(total_ratings)

    def view_all_movies(self):
        if not self.movies:
            return None
        return self.movies.values()