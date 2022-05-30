from db.run_sql import run_sql
from models.country import Country
from models.city import City
import repositories.country_repository as country_repository

def save(city):
    sql = "INSERT INTO cities (name, country_id, visited, id) VALUES (?, ?, ? ,?) RETURNING *"
    values = [city.name, city.country_id, city.visited, city.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        city = City(row['name'], row["country_id"], row["visited"], row['id'])
        cities.append(city)
    return cities


def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = ?"
    values = [id]
    results = run_sql(sql, values)[0]

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM cities WHERE id = ?"
    values = [id]
    run_sql(sql, values)

def update(city):
    sql = "UPDATE cities SET (name, country_id, visited, id) VALUES (?, ?, ? ,?) WHERE id = ?"
    values = [city.name, city.country_id, city.visited, city.id]
    run_sql(sql, values)