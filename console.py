import pdb
from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

country_repository.delete_all()
city_repository.delete_all()

country1 = Country("Italy")
country_repository.save(country1)

country2 = Country("Germany")
country_repository.save(country2)

country_repository.select_all()

city1 = City("Rome", country1, True)
city_repository.save(city1)

city2 = City("Berlin", country2, False)
city_repository.save(city2)

pdb.set_trace()
