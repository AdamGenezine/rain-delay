import pandas as pd


class FlightPreprocessor:

    COLUMN_MAPPING = {
        "Sigla ICAO Empresa Aérea": "airline_icao",
        "Empresa Aérea": "airline",
        "Número Voo": "flight_number",
        "Modelo Equipamento": "aircraft_model",
        "Número de Assentos": "number_of_seats",
        "Sigla ICAO Aeroporto Origem": "origin_airport",
        "Descrição Aeroporto Origem": "origin_airport_name",
        "Partida Prevista": "scheduled_departure",
        "Partida Real": "actual_departure",
        "Sigla ICAO Aeroporto Destino": "destination_airport",
        "Descrição Aeroporto Destino": "destination_airport_name",
        "Chegada Prevista": "scheduled_arrival",
        "Chegada Real": "actual_arrival",
        "Situação Voo": "flight_status",
    }

    DATETIME_COLUMNS = [
        "scheduled_departure",
        "actual_departure",
        "scheduled_arrival",
        "actual_arrival",
    ]

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()

        df = self._rename_columns(df)
        df = self._convert_datetime_columns(df)
        df = self._calculate_delays(df)

        return df

    def _rename_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.rename(columns=self.COLUMN_MAPPING)

    def _convert_datetime_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        for column in self.DATETIME_COLUMNS:
            df[column] = pd.to_datetime(
                df[column],
                format="%d/%m/%Y %H:%M",
                errors="coerce",
            )

        return df

    def _calculate_delays(self, df: pd.DataFrame) -> pd.DataFrame:
        df["departure_delay_minutes"] = (
            df["actual_departure"] - df["scheduled_departure"]
        ).dt.total_seconds() / 60

        df["arrival_delay_minutes"] = (
            df["actual_arrival"] - df["scheduled_arrival"]
        ).dt.total_seconds() / 60

        return df