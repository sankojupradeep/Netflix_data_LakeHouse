import dlt
from pyspark.sql.functions import col

@dlt.table(name="movie_gold")
def movie_gold():
    movies = spark.readStream.table("movie_silver")
    links = spark.readStream.table("linkS")

    return (
        movies.alias("m")
        .join(links.alias("l"), col("m.movieId") == col("l.movieId"), "inner")
        .select(
            col("m.movieId"),
            col("m.title"),
            col("m.genres"),
            col("l.imdbId"),
            col("l.tmdbId")
        )
    )
