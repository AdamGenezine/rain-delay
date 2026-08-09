from pathlib import Path

import pandas as pd


class WeatherProcessor:

    def __init__(self, weather_dir: str = "data/raw/weather"):
        self.weather_dir = Path(weather_dir)

    def load(self) -> pd.DataFrame:
        files = list(self.weather_dir.glob("*.parquet"))

        if not files:
            raise FileNotFoundError(
                f"No weather files found in {self.weather_dir}"
            )

        dataframes = []

        for file in files:
            df = pd.read_parquet(file)
            dataframes.append(df)

        weather = pd.concat(
            dataframes,
            ignore_index=True,
        )

        return weather

    def save(
        self,
        weather: pd.DataFrame,
        output_path: str = "data/processed/weather.parquet",
    ) -> None:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        weather.to_parquet(
            output_path,
            index=False,
        )

        print(f"Saved: {output_path}")