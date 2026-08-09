from rain_delay.data.flight_downloader import FlightDownloader


downloader = FlightDownloader()

downloader.download_range(
    start_year=2022,
    end_year=2025,
)