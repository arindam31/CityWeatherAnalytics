import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound


def create_tables(db_engine, base):
    base.metadata.create_all(db_engine)


def create_db(name):
    _engine = sqlalchemy.create_engine(f'sqlite:///{name}.db', echo=False)
    return _engine


def create_session_class(engine):
    cls_session = sessionmaker(bind=engine)
    return cls_session


def connect_db(name):
    _engine = create_db(name)
    cls_session = create_session_class(_engine)
    session_obj = create_session(cls_session)
    return session_obj


def create_session(cls_session):
    session_obj = cls_session()
    return session_obj


if __name__ == '__main__':
    from model import Continent, Country, City, Weather
    db_name = 'locations'
    engine = create_db(db_name)

    # Base.metadata.drop_all(bind=engine, tables=[Weather.__table__])  # Remove a table
    # print('Create DB')
    # create_tables(engine)
    print('Creating tables')
    Session = create_session_class(engine)

    session = create_session(Session)

    # Weather.__table__.create(session.bind) # To add a new table
    # sess = connect_db(db_name)

    # Get all countries in a continent

    # countries_in_continent = sess.query(Country).filter(Country.continent.has(continent_code='OC')).all()
    # for c in countries_in_continent:
    #     print(c.name, c.country_code)
    #
    # # Get All cities in a country
    # country_code = 'PG'
    # cities_in_country = sess.query(City).filter(City.country.has(country_code=country_code)).all()
    # print(len(cities_in_country))

    # Get all cities in continent.
    # cities_in_continent = sess.query(City).filter(Country.continent.has(continent_code='AN')).all()
    # print(cities_in_continent)
    #
    # city_list = ['New Delhi', 'Shanghai', 'Bangkok', 'Beijing',
    #              'Nairobi', 'Cape Town', 'Harare', 'Mombasa',
    #              'Innsbruck', 'Munich', 'Bologna', 'Marseille',
    #              'Esperahza Base', 'Orcadas', 'Villalos', 'Carlini Base',
    #              'Honiara', 'Canberra', 'Auckland', 'Gold Coast',
    #              'Seattle', 'Mexico City', 'Arizona City', 'Chicago Heights',
    #              'Caracas', 'Panama City', 'Curitiba', 'Bogota'
    #              ]
    #
    # for city_name in city_list:
    #     try:
    #         #got_city = sess.query(City).filter(City.name.contains(city_name)).one()
    #         got_city = sess.query(City).filter(City.name == city_name).one()
    #         print(got_city)
    #         print(city_name, got_city.city_id)
    #         print(got_city.country, got_city.country.continent.name)
    #         print('---------------------------')
    #     except MultipleResultsFound as e:
    #         print(f'Whoooa..there is more than one city: {city_name}?')
    #         all_cities_found = sess.query(City).filter(City.name.contains(city_name)).all()
    #         print('Found all same city:', all_cities_found)
    #
    #     except NoResultFound:
    #         print(f'Perhaps city {city_name} is not there !!!!!')




