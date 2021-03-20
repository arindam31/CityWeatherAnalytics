import csv
import json

from helper import connect_db
from model import Continent, City, Country, Weather


def write_continent_to_db(line_to_write):
    if not sess.query(Continent).filter_by(continent_code=line_to_write['Continent_Code']).all():
        continent = Continent(
            name=line_to_write['Continent_Name'],
            continent_code=line_to_write['Continent_Code'])
        sess.add(continent)
        sess.commit()


def write_cities_to_db(line_to_write):
    if not sess.query(City).filter_by(continent_code=line_to_write['Continent_Code']).all():
        continent = Continent(
            name=line_to_write['Continent_Name'],
            continent_code=line_to_write['Continent_Code'])
        sess.add(continent)
        sess.commit()


def write_country_to_db(line_to_write):
    if not sess.query(Country).filter_by(country_code=line_to_write['country_code']).all():
        continent = sess.query(Continent).filter_by('')
        country = Country(
            name=line_to_write['country_full'],
            country_code=line_to_write['country_code'])
        sess.add(country)
        sess.commit()

def write_altitude_of_city():
    to_update = []
    count_not_found = 0
    count_found = 0
    with open('../../data/city_data.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            id, country, city, lat, lon, altitude = row
            #print(id, country, city, lat, lon, int(float(altitude)))

            try:
                the_city = sess.query(City).filter_by(name=city).all()[0]
                count_found += 1
                the_city.altitude = int(float(altitude))
                to_update.append(the_city)
            except IndexError:
                #print(f'City {city} not found')
                count_not_found += 1

    print(count_found, count_not_found)
    sess.bulk_save_objects(to_update)
    sess.commit()
    print ('Done !!!!')

def create_missing_country_city():


    to_save = []
    cnt_added = 0
    city_add = 0
    with open('../../data/json/finale.json') as ffop:
        data = json.load(ffop)
        for line in data:
            if 'continent_code' in line.keys():
                if not sess.query(Country).filter_by(country_code=line['country_code']).all():
                    continent = sess.query(Continent).filter_by(continent_code=line['continent_code']).all()[0]
                    continent_id = continent.id
                    country = Country(
                        name=line['country_full'],
                        country_code=line['country_code'],
                        continent_id=continent_id)
                    sess.add(country)
                    sess.commit()
                    print('Added a country:', line['country_full'])
                    cnt_added += 1
                    print (cnt_added)

                else:
                    country = sess.query(Country).filter_by(country_code=line['country_code']).all()[0]
                    city = City(name=line['city_name'],
                                city_id=line['city_id'],
                                country_id=country.id,
                                lat=line['lat'],
                                lon=line['lon']
                                )
                    city_add += 1
                    to_save.append(city)
                    print('Added a city:', line['city_name'])
                    print(city_add)

    sess.bulk_save_objects(to_save)
    sess.commit()



def calculate_write_mean_temp_to_weather(sess):
    # Read min_temp and max_temp of each entry in Weather
    to_update_mean = []
    all_weather_rows = sess.query(Weather).all()
    for row in all_weather_rows:
        min_temp = row.min_temp
        max_temp = row.max_temp

        # Calculate Mean
        mean = (min_temp + max_temp) / 2
        row.mean_temp = mean
        to_update_mean.append(row)

    # Write to column 'mean_temp' in table Weather
    sess.bulk_save_objects(to_update_mean)
    sess.commit()

def main():
    sess = connect_db('../../locations')


if __name__ == '__main__':
    main()

