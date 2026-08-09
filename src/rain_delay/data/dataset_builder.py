from pathlib import Path

import pandas as pd


class DatasetBuilder:

    def __init__(self, output_dir: str = "data/processed"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def build_flights(
        self,
        flights: pd.DataFrame,
        airports: pd.DataFrame,
    ) -> pd.DataFrame:
        flights_brazil = flights.merge(
            airports,
            left_on="origin_airport",
            right_on="airport_icao",
            how="inner",
        )

        return flights_brazil

    def build_airports(
        self,
        flights_brazil: pd.DataFrame,
    ) -> pd.DataFrame:
        airports = (
            flights_brazil[
                [
                    "origin_airport",
                    "airport_name",
                    "city",
                    "state",
                    "latitude",
                    "longitude",
                ]
            ]
            .drop_duplicates()
            .sort_values("origin_airport")
            .reset_index(drop=True)
        )

        return airports

    def save(
        self,
        flights: pd.DataFrame,
        airports: pd.DataFrame,
    ) -> None:
        flights.to_parquet(
            self.output_dir / "flights.parquet",
            index=False,
        )

        airports.to_parquet(
            self.output_dir / "airports.parquet",
            index=False,
        )