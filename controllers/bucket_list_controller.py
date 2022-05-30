from flask import Flask, render_template, request, redirect
import repositories.country_repository as country_repository
# from models.city import City
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
# GET '/tasks/new'


# CREATE
# POST '/tasks'


# SHOW
# GET '/tasks/<id>'


# EDIT
# GET '/tasks/<id>/edit'


# UPDATE
# PUT '/tasks/<id>'


# DELETE
# DELETE '/tasks/<id>'

# @countries_blueprint.route("/countries")
# def countries():
#     countries = country_repository.select_all() # NEW
#     return render_template("countries/index.html", all_countries = countries)
