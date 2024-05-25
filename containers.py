from dependency_injector import containers, providers
from services import Config, GeoapifyService, NominatimService
from dotenv import load_dotenv
import os

load_dotenv()
class Container(containers.DeclarativeContainer):
    """
    Container for dependency injection.

    Attributes:
        config (Config): The Config class.
        geoapify_service (GeoapifyService): The GeoapifyService class.
        nominatim_service (NominatimService): The NominatimService class.
    
    """
    geoapify_config = providers.Singleton(Config, api_key=os.getenv("geoapify_api_key"))
    geoapify_service = providers.Factory(GeoapifyService, config=geoapify_config)

    # secondary service for reverse geocoding
    nominatim_service = providers.Factory(NominatimService)

