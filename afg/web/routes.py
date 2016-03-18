from flask import Blueprint, url_for, redirect, render_template

blueprint = Blueprint('web', __name__,
    template_folder='templates'
)

@blueprint.route('/')
def home():
    return render_template('home.html')
