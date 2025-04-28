import sys
from datetime import datetime

from movie_rating_functions.movie_rating import Movie, MovieNotFoundError, InvalidRatingError, MovieAlreadyExistsError

def main_menu():
    movie_db = Movie()

    while True:
        print("\n===== MOVIE RATING APP =====")
        print("1. Add a Movie")
        print("2. Rate a Movie")
        print("3. Get Average Rating of a Movie")
        print("4. Get Overall Average Rating of All Movies")
        print("5. View All Movies")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            movie_name = input("Enter the movie name: ").strip().lower()
            try:
                movie_db.add_movie(movie_name)
                print(f"Movie {movie_name} added on {datetime.now().replace(microsecond=0).replace(microsecond=0)} successfully!")
            except MovieAlreadyExistsError as e:
                print(f"Error: {e}")

        elif choice == "2":
            movie_name = input("Enter the movie name: ").strip().lower()
            try:
                rating = int(input("Enter rating (1-5): ")).strip
                avg_rating = movie_db.movie_rating(movie_name, rating)
                print(f"New average rating for '{movie_name}': {avg_rating}")
            except (MovieNotFoundError, InvalidRatingError) as e:
                print(f"Error: {e}")
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 5.")

        elif choice == "3":
            movie_name = input("Enter the movie name: ").strip().lower()
            try:
                avg_rating = movie_db.get_average_rating(movie_name)
                if avg_rating is not None:
                    print(f"Average rating for '{movie_name}': {avg_rating}")
                else:
                    print(f"'{movie_name}' has no ratings yet.")
            except MovieNotFoundError as e:
                print(f"Error: {e}")

        elif choice == "4":
            avg_rating = movie_db.get_overall_average_rating()
            if avg_rating is not None:
                print(f"Overall average rating of all movies: {avg_rating}")
            else:
                print("No movies have been rated yet.")

        elif choice == "5":
            all_movie = movie_db.view_all_movies()
            if all_movie is not None:
                print(f"Movies viewed: {len(all_movie)}")

        elif choice == "6":
            print("Exiting the Movie Rating App. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main_menu()
