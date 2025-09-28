import dlt

dlt.create_streaming_table(
    name="link"
)

@dlt.append_flow(target="link")

def Link():
    df=spark.readStream.table("netflix_data.default.links")
    return df