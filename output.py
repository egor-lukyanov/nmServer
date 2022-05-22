from statistics import median
from flask import request, render_template, Blueprint

from app import app
from storage import all_metrics


@app.route('/', methods=['get'])
def get_info():

    return render_template("template.j2.html", data=all_metrics, agg=median)


bp = Blueprint('output', __name__)
