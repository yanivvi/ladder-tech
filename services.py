import requests
from requests.structures import CaseInsensitiveDict
from geopy.geocoders import Nominatim

class Config:
    def __init__(self, api_key: str):
        self.api_key = api_key


class GeoapifyService:
    def __init__(self, config: Config):
        self.api_key = config.api_key

    def get_country(self, lat: float, lon: float) -> str:
        """
        Get the country based on the given latitude and longitude coordinates.

        Parameters:
            lat (float): The latitude coordinate.
            lon (float): The longitude coordinate.

        Returns:
            str: The country name or 'no country found' if the country could not be determined.
        """

        url = f'https://api.geoapify.com/v1/geocode/reverse?lat={lat}&lon={lon}&apiKey={self.api_key}'
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        resp = requests.get(url, headers=headers)

        # If the country could not be determined, return 'no country found'
        try:
            country = resp.json()['features'][0]['properties']['country']
        except (KeyError, IndexError):
            return 'no country found'

        return country

class NominatimService:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="GetLoc")

    def get_country(self, lat: float, lon: float) -> str:
        """
        Get the country based on the given latitude and longitude coordinates. (using Nominatim api -  not in use but kept for reference) 

        Parameters:
            lat (float): The latitude coordinate.
            lon (float): The longitude coordinate.

        Returns:
            str: The country name or 'no country found' if the country could not be determined.
        """

        # If the country could not be determined, return 'no country found'
        try:
            location = self.geolocator.reverse(f"{lat}, {lon}")
            country = location.raw['address']['country']
        except Exception as e:
            country = 'no country found'

        return country


