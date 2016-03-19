from flask import Blueprint, url_for, redirect, render_template, request
import geojson
from afg.database.inject import inject_dao
from shapely.geometry import mapping, shape
import json
from afg.models import *

blueprint = Blueprint('web', __name__,
    template_folder='templates'
)

@blueprint.route('/')
def home():
    return render_template('home.html')

@blueprint.route('/game')
def game():
    return render_template('map.html')

@blueprint.route('/check', methods=['POST'])
@inject_dao
def check(dao):
    data = request.get_json(force=True)
    geom = shape(data)
    roads = [Road(*r).__geo_interface__ for r in dao.problems(geom=geom)]
    #return json.dumps(roads)
    return geojson.dumps(geojson.FeatureCollection(roads))
