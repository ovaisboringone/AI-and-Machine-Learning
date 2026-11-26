import pandas as pd

ratings = pd.read_csv(
    "u.data",
    sep="\t",
    names=["user_id", "movie_id", "rating", "timestamp"]
)

movies = pd.read_csv(
    "u.item",
    sep="|",
    encoding="latin-1",
    header=None,
    usecols=[0, 1],
    names=["movie_id", "movie_title"]
)

print("Ratings Data:")
print(ratings.head())

print("\nMovie Data:")
print(movies.head())

movie_stats = ratings.groupby("movie_id").agg(
    AverageRating=("rating", "mean"),
    RatingCount=("rating", "count")
).reset_index()

final_data = pd.merge(movie_stats, movies, on="movie_id", how="inner")

final_data["AverageRating"] = final_data["AverageRating"].round(2)

print("\nMovie Statistics:")
print(final_data.head(10))

print("\nTop 10 Movies by Average Rating:")
print(final_data.sort_values("AverageRating", ascending=False).head(10))