from pathlib import Path

import pandas as pd
import requests


class WeatherClient:

    BASE_URL = "https://archive-api.open-meteo.com/v1/archive"

    HOURLY_VARIABLES = [
        "precipitation",
        "temperature_2m",
        "relative_humidity_2m",
        "wind_speed_10m",
        "wind_gusts_10m",
        "weather_code",
    ]

    def __init__(self, output_dir: str = "data/raw/weather"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def download_airport(
        self,
        airport_icao: str,
        latitude: float,
        longitude: float,
        start_date: str,
        end_date: str,
    ) -> pd.DataFrame:

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "start_date": start_date,
            "end_date": end_date,
            "hourly": ",".join(self.HOURLY_VARIABLES),
            "timezone": "auto",
        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=120,
        )

        response.raise_for_status()

        data = response.json()

        timezone = data["timezone"]

        df = pd.DataFrame(data["hourly"])

        df = df.rename(
            columns={
                "time": "datetime",
            }
        )

        df["datetime"] = pd.to_datetime(df["datetime"])
        df["airport_icao"] = airport_icao
        df["timezone"] = timezone

        return df

    def save(
        self,
        df: pd.DataFrame,
        airport_icao: str,
    ) -> None:

        output_path = self.output_dir / f"{airport_icao}.parquet"

        df.to_parquet(
            output_path,
            index=False,
        )

        print(f"Saved: {output_path}")