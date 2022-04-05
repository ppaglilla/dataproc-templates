PROJECT_ID_PROP = "project.id"

# GCS to BigQuery
GCS_BQ_INPUT_LOCATION = "gcs.bigquery.input.location"
GCS_BQ_INPUT_FORMAT = "gcs.bigquery.input.format"
GCS_BQ_OUTPUT_DATASET = "gcs.bigquery.output.dataset"
GCS_BQ_OUTPUT_TABLE = "gcs.bigquery.output.table"
GCS_BQ_CSV_FORMAT = "csv"
GCS_BQ_AVRO_FORMAT = "avro"
GCS_BQ_PRQT_FORMAT = "parquet"
GCS_BQ_CSV_HEADER = "header"
GCS_BQ_OUTPUT_FORMAT = "com.google.cloud.spark.bigquery"
GCS_BQ_CSV_INFER_SCHEMA = "inferSchema"
GCS_BQ_TEMP_BUCKET = "temporaryGcsBucket"
GCS_BQ_LD_TEMP_BUCKET_NAME = "gcs.bigquery.temp.bucket.name"
GCS_BQ_OUTPUT = "table"
GCS_BQ_AVRO_EXTD_FORMAT = "com.databricks.spark.avro"


# BigQuery to GCS
BQ_GCS_INPUT_TABLE = "bigquery.gcs.input.table"
BQ_GCS_OUTPUT_FORMAT_CSV = "csv"
BQ_GCS_OUTPUT_FORMAT_AVRO = "avro"
BQ_GCS_OUTPUT_FORMAT_PARQUET = "parquet"
BQ_GCS_OUTPUT_FORMAT_JSON = "json"
BQ_GCS_OUTPUT_FORMAT = "bigquery.gcs.output.format"
BQ_GCS_OUTPUT_MODE_OVERWRITE = "overwrite"
BQ_GCS_OUTPUT_MODE_APPEND = "append"
BQ_GCS_OUTPUT_MODE="bigquery.gcs.output.mode"
BQ_GCS_OUTPUT_LOCATION = "bigquery.gcs.output.location"