import dlt
from pyspark.sql.functions import col

@dlt.table(name="gnme_gold")
def gnme_gold():
    gnme = dlt.read("gnme_silver")
    gnme2 = dlt.read("gnme2_silver")

    return (
        gnme.alias("g")
        .join(gnme2.alias("t"), col("g.tagId") == col("t.tagId"), "inner")
        .select(
            col("g.movieId"),
            col("g.tagId"),
            col("t.tag")  # Enriched tag description
        )
    )
