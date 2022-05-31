from db.run_sql import run_sql
from models.country import Country
from models.city import City
import repositories.country_repository as country_repository

def save(city):
    sql = "INSERT INTO cities (name, country, visited, id) VALUES (?, ?, ? ,?) RETURNING *"
    values = [city.name, city.country.id, city.visited, city.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        visited = True if row["visited"] == 1 else False
        country = country_repository.select(row["country"])
        city = City(row["name"], country, visited, row["id"])
        cities.append(city)
    return cities


def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = ?"
    values = [id]
    results = run_sql(sql, values)[0]

    if result is not None:
        visited = True if row["visited"] == 1 else False
        country = country_repository.select(result ["country"])
        city = City(result['name'], result['country'], result['id'])
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM cities WHERE id = ?"
    values = [id]
    run_sql(sql, values)

def update(city):
    sql = "UPDATE cities SET (name, country, visited, id) VALUES (?, ?, ? ,?) WHERE id = ?"
    values = [city.name, city.country, city.visited, city.id]
    run_sql(sql, values)



