from flask import Flask, Response, make_response
from flask_restful import reqparse
from imsakiyah import generate

app = Flask(__name__)

parser = reqparse.RequestParser()
parser.add_argument('lat')
parser.add_argument('long')
parser.add_argument('start')
parser.add_argument('days')

@app.route('/imsakiyah/<string:lat>/<string:lon>/<string:date>/<int:days>')
def imsakiyah(lat,lon,date,days):

    cal = generate(lat, lon, date, days)

    file_name = 'jadwal_imsakiyah_%s_%s.ics' % (lat, lon)

    return Response(
        cal,
        headers={"Content-disposition":
                     "attachment; filename={}".format(file_name)})
