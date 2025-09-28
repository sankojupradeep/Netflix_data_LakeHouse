import dlt
from pyspark.sql.functions import col

@dlt.table(name="rating_gold")
def rating_gold():
    movies = dlt.read("movie_gold")
    ratings = dlt.read("rating_silver")

    return (
        ratings.alias("r")
        .join(movies.alias("m"), col("r.movieId") == col("m.movieId"), "inner")
        .select(
            col("r.userId"),
            col("r.movieId"),
            col("m.title"),
            col("m.genres"),
            col("r.rating")
        )
    )
