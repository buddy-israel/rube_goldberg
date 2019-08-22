from flask import Flask, render_template
import json
import requests

app = Flask(__name__)
@app.route('/')

def index():
    r = requests.get('https://bvg-grabber-api.herokuapp.com/actual?station=Oderbruchstrasse&vehicles=Tram').json()
    data = r[0][1]
    Trains = []
    for train in data:
        if not 'Zingster' in train['end'] and not 'Marzahn' in train['end'] and not 'Hellersdorf' in train['end']:
            Trains.append(train)

    return render_template('home.html', Trains=Trains)
    time.sleep(30)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
