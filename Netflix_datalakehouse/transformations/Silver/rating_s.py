import dlt

@dlt.view(
    name="rating_view"
)

def rating_view():
    return spark.readStream.table("rating")

dlt.create_streaming_table(
    name="rating_silver"
)

dlt.create_auto_cdc_flow(
    target="rating_silver",
    source="rating_view",
    keys = ["userId"],
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