import xml.etree.ElementTree as ET
import requests


class AviationWeatherClient:

    def __init__(self):
        # The modern official NOAA AWC API endpoint
        self.base_url = "https://aviationweather.gov/api/data/metar"

    def fetch_raw_metar(self, station_id: str) -> str:
        """Fetches the raw METAR string for a given airport ICAO code in XML format."""
        # Clean up the station ID input (ensure uppercase)
        station_id = station_id.strip().upper()

        # Set up the query parameters for the new API layout
        params = {"ids": station_id, "format": "xml"}

        try:
            # Send the GET request to aviationweather.gov
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()

            # Parse the XML response
            root = ET.fromstring(response.content)

            # Find the raw text inside the XML structure
            # The AWC XML format nests the data inside <METAR><raw_text>
            raw_text_element = root.find(".//raw_text")

            if raw_text_element is not None and raw_text_element.text:
                return raw_text_element.text.strip()
            else:
                return f"Error: No METAR data found for station '{station_id}'."

        except requests.exceptions.RequestException as e:
            return f"Network/API Error: Could not retrieve data. Details: {e}"
        except ET.ParseError:
            return "Error: Failed to parse XML response from server."