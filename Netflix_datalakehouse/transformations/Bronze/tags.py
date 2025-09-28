import dlt

dlt.create_streaming_table(
    name="Tag"
)

@dlt.append_flow(target="Tag")

def tag_():
    df=spark.readStream.table("netflix_data.default.tags")
    return df