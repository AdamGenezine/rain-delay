from pathlib import Path

import requests


class FlightDownloader:
    BASE_URL = "https://siros.anac.gov.br/siros/registros/diversos/vra"

    def __init__(self, output_dir: str = "data/raw/flights"):
        self.output_dir = Path(output_dir)

    def download_year(self, year: int) -> None:
        year_dir = self.output_dir / str(year)
        year_dir.mkdir(parents=True, exist_ok=True)

        for month in range(1, 13):
            filename = f"VRA_{year}_{month:02d}.csv"
            url = f"{self.BASE_URL}/{year}/{filename}"
            output_path = year_dir / filename

            self._download_file(url, output_path)

    def download_range(self, start_year: int, end_year: int) -> None:
        for year in range(start_year, end_year + 1):
            print(f"\nDownloading year {year}...")
            self.download_year(year)

    @staticmethod
    def _download_file(url: str, output_path: Path) -> None:
        if output_path.exists():
            print(f"Skipping: {output_path}")
            return

        response = requests.get(url, timeout=60)

        if response.status_code == 404:
            print(f"Not found: {url}")
            return

        response.raise_for_status()

        output_path.write_bytes(response.content)

        print(f"Downloaded: {output_path}")