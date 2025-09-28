import dlt

dlt.create_streaming_table(
    name="geoname_score"
)

@dlt.append_flow(target="geoname_score")

def Gename():
    df=spark.readStream.table("netflix_data.default.Genome_scores")
    return df