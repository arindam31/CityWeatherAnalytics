import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir))

from utils.weather.api_weather import create_payload, call_api, get_date, get_temp_from_response, KEY
from utils.db.helper import connect_db
from utils.db.model import City, Weather


city_list = ['New Delhi', 'Shanghai', 'Bangkok', 'Beijing',
             'Nairobi', 'Cape Town', 'Harare', 'Mombasa',
             'Innsbruck', 'Munich', 'Bologna', 'Marseille',
             'Honiara', 'Canberra', 'Auckland', 'Gold Coast',
             'Seattle', 'Mexico City', 'Arizona City', 'Chicago Heights',
             'Caracas', 'Panama City', 'Curitiba', 'Bogota'
             ]


def create_session():
    """Get a session."""
    db_name = '../locations'
    session = connect_db(db_name)
    return session


def main(session):
    """Main function.

    :param session: session to write and access data.
    """
    to_write = []

    # For each city, get city id from db
    for city_name in city_list:
        got_city = session.query(City).filter(City.name == city_name).one()
        city_id = got_city.city_id
        city_lat = got_city.lat
        city_lon = got_city.lon
        print(city_id)

        # For D days, create payload. For free account, only 1 day can be requested in 1 request.
        D = 15
        start_date = '2021-01-01'

        # Loop for D days
        for _ in range(D):
            # Create payload.
            end_date = get_date(start_date, 1)
            payload = create_payload(key=KEY, lat=city_lat, lon=city_lon, start_date=start_date, end_date=end_date)
            start_date = end_date

            # Call api
            response = call_api(payload)

            # Get temperatures from data.
            max_temp, min_temp, date = get_temp_from_response(response)

            # Write data collected to weather table
            weather = Weather(
                min_temp=min_temp,
                max_temp=max_temp,
                mean_temp=(min_temp + max_temp)/2,
                city_id=city_id,
                timestamp=get_date(date, to_string=False)
            )
            to_write.append(weather)

    session.bulk_save_objects(to_write)
    session.commit()



if __name__ == '__main__':
    sess = create_session()
    main(session=sess)
