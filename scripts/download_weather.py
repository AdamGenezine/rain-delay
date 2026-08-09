import time
from pathlib import Path

import pandas as pd
import requests

from rain_delay.data.weather_client import WeatherClient


AIRPORTS_PATH = Path("data/processed/airports.parquet")
WEATHER_DIR = Path("data/raw/weather")

START_DATE = "2022-01-01"
END_DATE = "2025-12-31"


def main() -> None:
    airports = pd.read_parquet(AIRPORTS_PATH)

    client = WeatherClient(
        output_dir=WEATHER_DIR,
    )

    total = len(airports)

    for index, airport in airports.iterrows():
        airport_icao = airport["origin_airport"]
        output_path = WEATHER_DIR / f"{airport_icao}.parquet"

        if output_path.exists():
            print(f"[{index + 1}/{total}] {airport_icao} - already exists")
            continue

        print(f"[{index + 1}/{total}] Downloading {airport_icao}...")

        try:
            weather = client.download_airport(
                airport_icao=airport_icao,
                latitude=airport["latitude"],
                longitude=airport["longitude"],
                start_date=START_DATE,
                end_date=END_DATE,
            )

            client.save(
                df=weather,
                airport_icao=airport_icao,
            )

        except requests.exceptions.HTTPError as error:
            if error.response.status_code == 429:
                print("Rate limit reached. Stopping download.")
                break

            print(f"Error downloading {airport_icao}: {error}")

        except Exception as error:
            print(f"Error downloading {airport_icao}: {error}")

        time.sleep(5)


if __name__ == "__main__":
    main()