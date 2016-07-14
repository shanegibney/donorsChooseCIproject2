from flask import Flask, Response, render_template
import json
import urllib2

app = Flask(__name__)

@app.route('/')
def test():
    return render_template('index.html')

@app.route('/funding')
def fundingByState():
    donors_choose_url = "http://api.donorschoose.org/common/json_feed.html?historical=true&APIKey=DONORSCHOOSE"
    response = urllib2.urlopen(donors_choose_url)
    json_response = json.load(response)
    return json.dumps(json_response)

if __name__ == '__main__':
    app.run()
