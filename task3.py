
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


data = {
    "title": [
        "The Dark Knight",
        "Inception",
        "Interstellar",
        "The Matrix",
        "Avengers: Endgame",
        "Iron Man",
        "Titanic",
        "The Notebook"
    ],
    "genre": [
        "Action Crime Drama",
        "Action Sci-Fi Thriller",
        "Adventure Drama Sci-Fi",
        "Action Sci-Fi",
        "Action Adventure Sci-Fi",
        "Action Adventure Sci-Fi",
        "Romance Drama",
        "Romance Drama"
    ]
}


movies = pd.DataFrame(data)


vectorizer = TfidfVectorizer(stop_words="english")
genre_matrix = vectorizer.fit_transform(movies["genre"])


similarity_matrix = cosine_similarity(genre_matrix, genre_matrix)


def recommend(movie_title, num_recommendations=3):
    if movie_title not in movies["title"].values:
        return f" Movie '{movie_title}' not found in database."
    
   
    idx = movies[movies["title"] == movie_title].index[0]
    
    
    sim_scores = list(enumerate(similarity_matrix[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    
   
    recommended = [movies.iloc[i[0]]["title"] for i in sim_scores]
    
    return recommended


print("🎬 Movie Recommendations Example:")
print("If you like 'Inception', you may also like:", recommend("Inception"))
print("If you like 'Titanic', you may also like:", recommend("Titanic"))

while True:
    user_input = input("\nEnter a movie you like (or 'quit' to exit): ")
    if user_input.lower() == "quit":
        print(" Thanks for using the movie recommender!")
        break
    print(" Recommendations:", recommend(user_input))

