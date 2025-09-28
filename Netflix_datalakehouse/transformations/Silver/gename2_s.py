import dlt

@dlt.view(
    name="gnme2_view"
)

def gnme_view():
    return spark.readStream.table("geoname_ta")

dlt.create_streaming_table(
    name="gnme2_silver"
)

dlt.create_auto_cdc_flow(
    target="gnme2_silver",
    source="gnme2_view",
    keys = ["tagId"],
    sequence_by = "tag",
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