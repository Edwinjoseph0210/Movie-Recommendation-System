"""
Movie Recommendation Demo

Suggest movies based on user input preferences.

Usage:
Run script and enter favorite genres.

"""

movies = {
    "Action": ["Mad Max", "John Wick", "Gladiator"],
    "Comedy": ["The Mask", "Superbad", "Step Brothers"],
    "Drama": ["The Shawshank Redemption", "Forrest Gump", "Fight Club"],
    "Sci-Fi": ["Inception", "Interstellar", "The Matrix"]
}

def recommend(genre):
    return movies.get(genre.title(), ["No recommendations available for this genre."])

def main():
    print("Enter your favorite movie genre ('exit' to quit):")
    while True:
        genre = input("> ")
        if genre.lower() == 'exit':
            break
        recommendations = recommend(genre)
        print("Recommended Movies:")
        for m in recommendations:
            print("-", m)

if __name__ == "__main__":
    main()
