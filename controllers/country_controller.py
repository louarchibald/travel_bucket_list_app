from flask import Flask, render_template, request, redirect
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
from models.city import City
from models.country import Country

from flask import Blueprint


countries_blueprint = Blueprint("countries", __name__)
# cities_blueprint = Blueprint("cities", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/countries'
@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all() # NEW
    return render_template("countries/index.html", all_countries = countries)


# NEW
# GET '/countries/new'
@countries_blueprint.route("/countries/new")
def new_country():
    countries = country_repository.select_all()
    return render_template("countries/new.html", all_countries = countries)


# CREATE
# POST '/tasks'
@countries_blueprint.route("/countries", methods=["POST"])
def create_country():
    # This is info from the database being added to the form
    name = request.form["name"]
    # This is saving to the form/database
    country = Country(name)
    country_repository.save(country)
    # Takes us back to countries page
    return redirect ("/countries")


# SHOW
# GET '/tasks/<id>'
@countries_blueprint.route("/countries/<id>", methods=["GET"])
def show_country(id):
    country = country_repository.select(id)
    return render_template("countries/show.html", country=country)


# EDIT
# GET '/tasks/<id>/edit'
@countries_blueprint.route("/countries/<id>/edit", methods=["GET"])
def edit_country(id):
    country = country_repository.select(id)
    cities = city_repository.select_all()
    return render_template("countries/edit.html", country=country, city=city)

# UPDATE
# PUT '/tasks/<id>'
@countries_blueprint.route("/countries/<id>", methods=["POST"])
def update_country(id):
    name = request.form["name"]
    continent = request.form["continent"]

    country = country_repository.select(id)
    country_repository.update(country)
    return redirect("/countries")



# DELETE
# DELETE '/tasks/<id>'
@countries_blueprint.route("/countries/<id>/delete", methods=["POST"])
def delete_task(id):
    country_repository.delete(id)
    return redirect("/countries")


