import dlt

@dlt.view(
    name="link_s"
)

def link_s():
    return spark.readStream.table("link")

dlt.create_streaming_table(
    name="linkS"
)

dlt.create_auto_cdc_flow(
    target="linkS",
    source="link_s",
    keys = ["movieId"],
    sequence_by = "imdbId",
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