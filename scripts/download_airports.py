from rain_delay.data.airport_downloader import AirportDownloader


AIRPORTS_URL = (
    "https://sistemas.anac.gov.br/dadosabertos/"
    "Aerodromos/Aeródromos%20Públicos/"
    "Lista%20de%20aeródromos%20públicos/"
    "AerodromosPublicos.csv"
)


downloader = AirportDownloader()
downloader.download(AIRPORTS_URL)