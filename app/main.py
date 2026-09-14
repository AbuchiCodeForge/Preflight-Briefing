"""
FastAPI application.
"""

from fastapi import FastAPI

app = FastAPI(title="Flight Briefer")

@app.get("/")
def read_root():
    fetcher = MetarFetcher()

    # Fetching KJFK
    station = "KJFK"
    raw_metar = fetcher.fetch_raw_metar(station)

    print(f"--- Raw METAR for {station} ---")
    print(raw_metar)