from containers import Container
import logging


def process_file(self, file_path: str):
        """
        Process a file containing latitude and longitude coordinates and print the country for each line.

        Parameters:
            file_path (str): The path to the file containing GPS data.
            use_geoapify (bool): Whether to use Geoapify for reverse geocoding. Defaults to True.
        """
        with open(file_path, 'r') as file:
            locations = file.readlines()

        for line in locations:
            _, lat, lon, _ = line.split(',')
            lat = lat.strip()
            lon = lon.strip()

            try:
                country = self.get_country_geoapify(float(lat), float(lon))
            except Exception as e:
                country = f'no country found, {e}'
            
            return country


def main():
    """
    Main function that configures the logger, creates a dependency injection container, gets the Geoapify service,
    processes a file of GPS data, extracts latitude and longitude from each line, removes leading and trailing
    whitespace, uses the Geoapify service to get the country for each line, and prints the results.

    Parameters:
    None

    Returns:
    None
    """

    # Configure the logger
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    # Create the dependency injection container
    container = Container()

    # Get the service
    geoapify_service = container.geoapify_service()

    # Process the file of GPS data
    file_path = 'data/GPS Data.csv'
    with open(file_path, 'r') as file:
        locations = file.readlines()

    for line in locations:
        # extract latitude and longitude
        _, lat, lon, _ = line.split(',')

        # remove leading and trailing whitespace
        lat = lat.strip()
        lon = lon.strip()

        # use service to get country
        country = geoapify_service.get_country(lat, lon)

        # use service to log results
        logger.info(f"{lat}, {lon}, {country}")

if __name__ == "__main__":
    main()
