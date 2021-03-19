from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Continent(Base):
    __tablename__ = 'continent'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    continent_code = Column(String(3), nullable=False)

    def __repr__(self):
        return f'{self.name}_{self.continent_code}'


class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    country_code = Column(String(3), nullable=False)
    continent_id = Column(Integer, ForeignKey("continent.id"), nullable=False)
    continent = relationship(Continent)

    def __repr__(self):
        return f'{self.country_code}_{self.name}_{self.continent}'


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    city_id = Column(Integer)
    country_id = Column(Integer, ForeignKey("country.id"), nullable=False)
    country = relationship(Country)
    lat = Column(Numeric(9, 7))
    lon = Column(Numeric(9, 7))
    altitude = Column(Integer, default=0)

    def __repr__(self):
        return f'{self.name}'


class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True)
    min_temp = Column(Numeric(3, 1))
    max_temp = Column(Numeric(3, 1))
    city_id = Column(Integer, ForeignKey("city.id"), nullable=False)
    city = relationship(City)
    timestamp = Column(DateTime)
