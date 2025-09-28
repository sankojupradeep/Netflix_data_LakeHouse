import dlt

dlt.create_streaming_table(
    name="Rating"
)

@dlt.append_flow(target="Rating")

def ratings():
    df=spark.readStream.table("netflix_data.default.Ratings")
    return df