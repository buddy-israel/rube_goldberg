from flask import Flask, render_template
import json, urllib
import requests

app = Flask(__name__)

@app.route('/')


def index():
    return render_template(
    'home.html', start=start, line=line, remaining=remaining, end=end, time=time,
    start2=start2, line2=line2, remaining2=remaining2, end2=end2, time2=time2,
    start3=start3, line3=line3, remaining3=remaining3, end3=end3, time3=time3)

r = requests.get('https://bvg-grabber-api.herokuapp.com/actual?station=oderbruchstr&vehicles=Tram,S&limit=2')
data = r.json()



start = data[0][1][0]["start"]
line = data[0][1][0]["line"]
remaining = data[0][1][0]["remaining"]
end = data[0][1][0]["end"]

start2 = data[0][1][1]["start"]
line2 = data[0][1][1]["line"]
remaining2 = data[0][1][1]["remaining"]
end2 = data[0][1][1]["end"]

start3 = data[0][1][2]["start"]
line3 = data[0][1][2]["line"]
remaining3 = data[0][1][2]["remaining"]
end3 = data[0][1][2]["end"]

if remaining == 60:
    time = 1
elif remaining == 180:
    time = 3
elif remaining == 120:
    time = 2
else:
    time = 'delayed'

if remaining2 == 60:
    time2 = 1
elif remaining2 == 180:
    time2 = 3
elif remaining2 == 120:
    time2 = 2
else:
    time2 = 'delayed'

if remaining3 == 60:
    time3 = 1
elif remaining3 == 180:
    time3 = 3
elif remaining3 == 120:
    time3 = 2
else:
    time3 = 'delayed'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
