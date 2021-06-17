from math import trunc
from flask import Flask, jsonify, render_template,Response
import os
from youtubesearchpython import VideosSearch,Video



app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/youtube-data/<string:n>')
def youtubeMusic(n):
    videosSearch = VideosSearch(n, limit=1)

    videos = videosSearch.result()
    videos1 = videos['result']
    return jsonify(videos1)



if __name__ == "__main__":
    app.run(debug=True, port=5000)
