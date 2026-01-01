#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm
import click

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64",
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime",
]


def ingest_data(
    url: str,
    engine,
    target_table: str,
    chunksize: int = 100_000,
) -> None:
    df_iter = pd.read_csv(
        url,
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=chunksize,
    )

    first_chunk = next(df_iter)

    # Create/replace table schema
    first_chunk.head(0).to_sql(
        name=target_table,
        con=engine,
        if_exists="replace",
        index=False,
    )
    print(f"Table {target_table} created")

    # Insert first chunk
    first_chunk.to_sql(
        name=target_table,
        con=engine,
        if_exists="append",
        index=False,
    )
    print(f"Inserted first chunk: {len(first_chunk)}")

    # Insert remaining chunks
    for df_chunk in tqdm(df_iter, desc="Ingesting"):
        df_chunk.to_sql(
            name=target_table,
            con=engine,
            if_exists="append",
            index=False,
        )
        print(f"Inserted chunk: {len(df_chunk)}")

    print(f"Done ingesting to {target_table}")


@click.command()
@click.option("--pg-user", default="root", show_default=True, help="PostgreSQL username")
@click.option("--pg-pass", default="root", show_default=True, help="PostgreSQL password")
@click.option("--pg-host", default="localhost", show_default=True, help="PostgreSQL host")
@click.option("--pg-port", default="5432", show_default=True, help="PostgreSQL port")
@click.option("--pg-db", default="ny_taxi", show_default=True, help="PostgreSQL database name")
@click.option("--year", default=2021, type=int, show_default=True, help="Year of the data")
@click.option("--month", default=1, type=int, show_default=True, help="Month of the data (1-12)")
@click.option("--chunksize", default=100_000, type=int, show_default=True, help="Chunk size for ingestion")
@click.option("--target-table", default="yellow_taxi_data", show_default=True, help="Target table name")
def main(pg_user, pg_pass, pg_host, pg_port, pg_db, year, month, chunksize, target_table):
    if not (1 <= month <= 12):
        raise click.BadParameter("month must be between 1 and 12")

    url_prefix = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow"
    url = f"{url_prefix}/yellow_tripdata_{year:04d}-{month:02d}.csv.gz"

    engine = create_engine(f"postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}")

    ingest_data(
        url=url,
        engine=engine,
        target_table=target_table,
        chunksize=chunksize,
    )


if __name__ == "__main__":
    main()
