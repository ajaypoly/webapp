from distutils.log import debug
from flask import Flask, render_template
import lyrics
app = Flask(__name__)


@app.route("/")
def hello():
    artists = lyrics.get_all_artist()
    return render_template("index.html", artists=artists)


@app.route("/songs/<int:aid>")
def list_all_songs(aid):
    songs = lyrics.get_all_songs(aid)
    singer = lyrics.singer(aid)
    artists = lyrics.get_all_artist()
    return render_template("songlist.html", singer=singer, songs=songs, artists=artists,current=aid)


@app.route("/songs/<int:aid>/lyrics/<int:sid>")
def lyric(sid, aid):
    songs = lyrics.get_all_songs(aid)
    singer = lyrics.singer(aid)
    artists = lyrics.get_all_artist()
    lyric = lyrics.get_lyrics(sid)
    return render_template("lyrics.html", lyrics=lyric, singer=singer, songs=songs, artists=artists,current=aid,current_song=sid)


if __name__ == "__main__":
    app.run(debug=True)
