import psycopg2

def get_all_artist():
    conn = psycopg2.connect("dbname=lyrics")
    cur=conn.cursor()
    cur.execute("select id,name from artist" )  
    artists= cur.fetchall()
    return artists

def get_all_songs(aid):
    conn = psycopg2.connect("dbname=lyrics")
    cur=conn.cursor()
    cur.execute("select song.song_name, song.song_id from song,artist where artist.id = song.artist and artist.id=%s",(aid,))  
    songs= cur.fetchall()
    return songs

def get_lyrics(sid):
    conn = psycopg2.connect("dbname=lyrics")
    cur=conn.cursor()
    cur.execute("select lyrics,song_name from song where song_id=%s",(sid,))
    lyric= cur.fetchone()
    return lyric

def singer(artistid):
    conn = psycopg2.connect("dbname=lyrics")
    cur=conn.cursor()
    cur.execute("select id,name from artist where artist.id=%s",(artistid,))  
    singer= cur.fetchone()
    return singer