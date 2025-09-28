import dlt

@dlt.view(
    name="movie_view"
)

def movie_view():
    return spark.readStream.table("movie")

dlt.create_streaming_table(
    name="movie_silver"
)

dlt.create_auto_cdc_flow(
    target="movie_silver",
    source="movie_view",
    keys = ["movieId"],
    sequence_by = "title",
    ignore_null_updates = False,
    apply_as_deletes = None,
    apply_as_truncates = None,
    column_list = None,
    except_column_list = None,
    stored_as_scd_type = 2,
    track_history_column_list = None,
    track_history_except_column_list = None,
    name = None,
    once = False
)