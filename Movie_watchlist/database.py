import datetime
import sqlite3

CREATE_MOVIE_TABLE = """ CREATE TABLE IF NOT EXISTS movies(
id INTEGER PRIMARY KEY,
title TEXT,
release_timestamp REAL
);
"""

CREATE_USER_TABLE = """CREATE TABLE IF NOT EXISTS users(
    username TEXT PRIMARY KEY
) ;
"""

CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched(
    user_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY(user_username) REFERENCE users(username),
    FOREIGN KEY(movie_id) REFERENCE movies(id)
);
"""

INSERT_MOVIES = "INSERT INTO movies (title, release_timestamp) VALUES (?, ?);"
INSERT_USER = "INSERT INTO users(username) VALUES (?);"
DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = """SELECT movies.* FROM movies
 JOIN watched ON movies.id = watched.movie_id
 JOIN users ON watched.user_username = users.username
 WHERE user.username = ?;"""
INSERT_WATCHED_MOVIE = "INSERT INTO watched (user_username, user_id) VALUES (?, ?)"
SET_MOVIE_WATCHED = "UPDATE movies SET watched = 1 WHERE title = ?;"


connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIE_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)
        connection.execute(CREATE_USER_TABLE)

def add_user(username):
    with connection:
        connection.execute(INSERT_USER, (username,))

def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIES, (title, release_timestamp))


def get_movies(upcoming=False):
    with connection:
        cursor = connection.cursor()
        if upcoming:
            
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()


def watch_movies(username, title):
    with connection:        
        connection.execute(INSERT_WATCHED_MOVIE, (username, movie_id))


def get_watched_movies(username):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (username,))
        return cursor.fetchall()