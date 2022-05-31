from flask import Flask, render_template, request, redirect
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
from models.city import City
from models.country import Country

from flask import Blueprint


cities_blueprint = Blueprint("cities", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/countries'
@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all() # NEW
    return render_template("cities/index.html", all_cities = cities)


# NEW
# GET '/countries/new'
@cities_blueprint.route("/cities/new")
def new_city():
    cities = city_repository.select_all()
    return render_template("cities/new.html", all_cities = cities)


# CREATE
# POST '/tasks'
@cities_blueprint.route("/cities", methods=["POST"])
def create_city():
    # This is info from the database being added to the form
    name = request.form["name"]
    # This is saving to the form/database
    city = City(name)
    city_repository.save(city)
    # Takes us back to countries page
    return redirect ("/cities")


# SHOW
# GET '/tasks/<id>'
@cities_blueprint.route("/cities/<id>", methods=["GET"])
def show_city(id):
    city = city_repository.select(id)
    country = country_repository.select_all()
    return render_template("cities/show.html", country=country, city=city)


# EDIT
# GET '/tasks/<id>/edit'
@cities_blueprint.route("/cities/<id>/edit", methods=["GET"])
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template("cities/edit.html", country=country, city=city)

# UPDATE
# PUT '/tasks/<id>'
@cities_blueprint.route("/cities/<id>", methods=["POST"])
def update_city(id):
    name = request.form["name"]
    country = request.form["country"]
    visited = bool(int(request.form["visited"]))

    city = city_repository.select(id)
    city_repository.update(city)
    return redirect("/cities")


# DELETE
# DELETE '/tasks/<id>'
@cities_blueprint.route("/cities/<id>/delete", methods=["POST"])
def delete_task(id):
    city_repository.delete(id)
    return redirect("/cities")


