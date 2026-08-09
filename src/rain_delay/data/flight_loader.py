from pathlib import Path

import pandas as pd


class FlightLoader:

    def __init__(self, input_dir: str = "data/raw/flights"):
        self.input_dir = Path(input_dir)

    def load_all(self) -> pd.DataFrame:
        files = sorted(self.input_dir.rglob("*.csv"))

        if not files:
            raise FileNotFoundError(
                f"No CSV files found in {self.input_dir}"
            )

        dataframes = []

        for file in files:
            print(f"Loading: {file}")
            df = pd.read_csv(
                file,
                sep=";",
                encoding="utf-8",
            )
            dataframes.append(df)

        return pd.concat(
            dataframes,
            ignore_index=True,
        )