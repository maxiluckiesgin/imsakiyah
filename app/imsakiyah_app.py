from flask import Flask, Response, make_response
from flask_restful import reqparse
from imsakiyah import generate

app = Flask(__name__)

parser = reqparse.RequestParser()
parser.add_argument('lat')
parser.add_argument('long')
parser.add_argument('start')
parser.add_argument('days')

@app.route('/')
def manual():
    return "<h2> Cara Penggunaan </h2> </br>" \
           "https://imsakiyah.herokuapp.com/imsakiyah/&lt;lat>/&lt;lon>/&lt;startdate>/&lt;days> </br>" \
           "contoh : <a href='https://imsakiyah.herokuapp.com/imsakiyah/-7.797068/110.370529/2021-04-13/30'>https://imsakiyah.herokuapp.com/imsakiyah/-7.797068/110.370529/2021-04-13/30</a>" \
           "<h2>Import ke Calendar</h2> </br>" \
           "<p>Setelah Anda menjalankan perintah di atas, sebuah file <b>ics</b> akan terdownload." \
           "Silakan buka apps <b>Calendar</b> di OSX, klik <b>File > Import</b> lalu pilih file hasil download."


@app.route('/imsakiyah/<string:lat>/<string:lon>/<string:date>/<int:days>')
def imsakiyah(lat,lon,date,days):

    cal = generate(lat, lon, date, days)

    file_name = 'jadwal_imsakiyah_%s_%s.ics' % (lat, lon)

    return Response(
        cal,
        headers={"Content-disposition":
                     "attachment; filename={}".format(file_name)})
