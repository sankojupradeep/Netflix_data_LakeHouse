import dlt

dlt.create_streaming_table(
    name="geoname_ta"
)

@dlt.append_flow(target="geoname_ta")

def Gename_ta():
    df=spark.readStream.table("netflix_data.default.Genome_tags")
    return df