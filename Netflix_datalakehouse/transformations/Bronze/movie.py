import dlt

dlt.create_streaming_table(
    name="Movie"
)

@dlt.append_flow(target="Movie")

def movie_():
    df=spark.readStream.table("netflix_data.default.Movies")
    return df