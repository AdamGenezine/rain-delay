from pathlib import Path

import requests


class AirportDownloader:

    def __init__(self, output_dir: str = "data/raw/airports"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def download(self, url: str, filename: str = "airports.csv") -> None:
        output_path = self.output_dir / filename

        if output_path.exists():
            print(f"Skipping: {output_path}")
            return

        response = requests.get(url, timeout=60)
        response.raise_for_status()

        output_path.write_bytes(response.content)

        print(f"Downloaded: {output_path}")