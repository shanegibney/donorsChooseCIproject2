from flask import Flask, Response, render_template
import json
import urllib2

app = Flask(__name__)

@app.route('/')
def test():
    return 'Everything is running!'

if __name__ == '__main__':
    app.run()
