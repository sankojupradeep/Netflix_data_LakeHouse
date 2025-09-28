import dlt

@dlt.view(
    name="tag_view"
)

def gnme_view():
    return spark.readStream.table("tag")

dlt.create_streaming_table(
    name="tag_silver"
)

dlt.create_auto_cdc_flow(
    target="tag_silver",
    source="tag_view",
    keys = ["userId","movieId"],
    sequence_by = "timestamp",
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