import json
from helper import connect_db
from model import Continent, City, Country



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


sess = connect_db('locations')
#
# with open('../../CC.json') as job:
#     data = json.load(job)
#     for line in data:
#         write_continent_to_db(line)

# with open('../../cities_all.json') as job:
#     data = json.load(job)
#     for line in data:
#         print(line)
# to_save = []
# cnt_added = 0
# city_add = 0
# with open('../../finale.json') as ffop:
#     data = json.load(ffop)
#     for line in data:
#         if 'continent_code' in line.keys():
#             if not sess.query(Country).filter_by(country_code=line['country_code']).all():
#                 continent = sess.query(Continent).filter_by(continent_code=line['continent_code']).all()[0]
#                 continent_id = continent.id
#                 country = Country(
#                     name=line['country_full'],
#                     country_code=line['country_code'],
#                     continent_id=continent_id)
#                 sess.add(country)
#                 sess.commit()
#                 print('Added a country:', line['country_full'])
#                 cnt_added += 1
#                 print (cnt_added)
#
#             else:
#                 country = sess.query(Country).filter_by(country_code=line['country_code']).all()[0]
#                 city = City(name=line['city_name'],
#                             city_id=line['city_id'],
#                             country_id=country.id,
#                             lat=line['lat'],
#                             lon=line['lon']
#                             )
#                 city_add += 1
#                 to_save.append(city)
#                 print('Added a city:', line['city_name'])
#                 print(city_add)
#
# sess.bulk_save_objects(to_save)
# sess.commit()

